import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import re

from helpers.ui_theme import inject_theme, page_hero, COLORS

inject_theme()

page_hero(
    "RealtEase Assistant",
    "Your AI real estate companion for Mumbai — ask about availability, pricing patterns, "
    "and listing insights. Connect an external API in the sidebar for advanced chat.",
    badge="🤖 Dataset-Powered Chat",
)


def query_model_api(prompt):
    url = st.session_state.get("realtEase_api_url", "").strip()
    if not url:
        return "Error contacting model API: API URL not set"
    try:
        response = requests.post(url, json={"prompt": prompt}, timeout=60)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Error contacting model API: {e}"


@st.cache_data
def load_data():
    return pd.read_csv("data/processed/mumbai.csv")


df = load_data()

st.sidebar.markdown(
    f"""
    <div style="background:{COLORS['accent_soft']};border-radius:12px;padding:1rem;
                border:1px solid {COLORS['border']};margin-bottom:1rem;">
        <p style="margin:0 0 0.5rem 0;font-weight:600;color:{COLORS['primary_dark']};">
            RealtEase Settings
        </p>
        <p style="margin:0;font-size:0.85rem;color:{COLORS['text_muted']};line-height:1.5;">
            Optional chatbot API URL. Leave blank to use local dataset answers.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.sidebar.text_input(
    "API URL",
    key="realtEase_api_url",
    placeholder="https://xxxx.ngrok-free.app/chat",
    label_visibility="collapsed",
)


def _extract_locality(text: str) -> str | None:
    m = re.search(r"\bin\s+([a-zA-Z ]{3,})$", text.strip(), flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().lower()
    for loc in df["LOCALITY_NAME"].astype(str).str.lower().unique():
        if loc and loc in text.lower():
            return loc
    return None


def local_answer(question: str) -> str:
    q = question.strip().lower()
    locality = _extract_locality(question)

    if locality:
        sub = df[df["LOCALITY_NAME"].astype(str).str.lower() == locality].copy()
        if sub.empty:
            return f"I couldn't find listings for **{locality}** in the dataset."

        n = len(sub)
        avg_price = sub["PRICE"].astype(float).mean()
        med_area = sub["AREA"].astype(float).median()
        top_bhk = (
            sub["BEDROOM_NUM"]
            .dropna()
            .astype(float)
            .round()
            .value_counts()
            .head(3)
            .to_dict()
        )

        show_cols = ["LOCALITY_NAME", "PRICE", "AREA", "BEDROOM_NUM", "FURNISH", "FLOOR_NUM"]
        sample = sub[show_cols].head(10)
        st.dataframe(sample, use_container_width=True)

        bhk_txt = ", ".join([f"{int(k)}BHK: {v}" for k, v in top_bhk.items()]) if top_bhk else "N/A"
        return (
            f"**Availability in {locality.title()} (from dataset):** {n} listings\n\n"
            f"- **Avg price**: ₹{avg_price:,.0f}\n"
            f"- **Median area**: {med_area:,.0f} sq.ft\n"
            f"- **Top BHK mix**: {bhk_txt}\n\n"
            "I also displayed the first 10 matching listings above."
        )

    if "what do you do" in q or "who are you" in q:
        return (
            "I answer questions using the local Mumbai dataset (availability, prices, patterns). "
            "If you provide an API URL in the sidebar, I can also forward queries to that chatbot."
        )

    return (
        "Ask me something like: **Is there any rooms available in Mulund West**, "
        "**average price in Andheri**, or **show area vs price**."
    )


SUGGESTIONS = [
    "What is the average price of a 2 BHK in Andheri?",
    "Is there any rooms available in Mulund West?",
    "Show area vs price trend",
    "What do you do?",
]

st.markdown(
    f"""
    <div class="re-section" style="padding:1rem 1.25rem;margin-bottom:1rem;">
        <p style="margin:0 0 0.6rem 0;font-weight:600;color:{COLORS['primary_dark']};">
            Try asking
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

s_cols = st.columns(len(SUGGESTIONS))
for i, suggestion in enumerate(SUGGESTIONS):
    with s_cols[i]:
        if st.button(suggestion, key=f"suggest_{i}", use_container_width=True):
            st.session_state["pending_query"] = suggestion

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pending = st.session_state.pop("pending_query", None)
user_query = st.chat_input("Ask me anything about Mumbai real estate...") or pending

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("RealtEase is thinking..."):
            prompt = f"""You are RealtEase, a real estate assistant trained on Mumbai housing data.
If the query is a question, answer normally.
If the query needs a chart or plot, return Python code only — using pandas and plotly — with no explanation.

Query: {user_query}
Response:"""

            final_resp = query_model_api(prompt)

            if isinstance(final_resp, str) and final_resp.startswith("Error contacting model API:"):
                final_resp = local_answer(user_query)
                st.markdown(final_resp)
            else:
                if "df[" not in final_resp:
                    final_resp = final_resp.split("Query:")[0].strip()

                if "import" in final_resp or "df[" in final_resp or "px." in final_resp:
                    try:
                        local_vars = {"df": df, "px": px, "st": st}
                        exec(final_resp, {}, local_vars)
                    except Exception as e:
                        st.error(f"Error executing code: {e}")
                else:
                    st.markdown(final_resp)

        st.session_state.messages.append({"role": "assistant", "content": final_resp})
