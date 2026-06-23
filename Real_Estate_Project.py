import streamlit as st
from helpers.bootstrap import ensure_model_artifacts
from helpers.ui_theme import inject_theme, page_hero, feature_card, section_box

st.set_page_config(
    page_title="Mumbai Real Estate Intelligence",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_theme()

with st.spinner("Preparing ML model (first run only)..."):
    ensure_model_artifacts()

page_hero(
    "Mumbai Real Estate Intelligence",
    "Explore rental patterns, predict property prices, and chat with your data — "
    "all in one soothing, interactive dashboard built for Mumbai's housing market.",
    badge="🏙️ Rental Insights & Price Prediction",
)

st.markdown("### Explore the modules")
col1, col2, col3 = st.columns(3)

with col1:
    feature_card(
        "📊",
        "Analytics",
        "Interactive maps, price trends, word clouds, and BHK distribution charts across Mumbai localities.",
        delay="0.05s",
    )
with col2:
    feature_card(
        "🔮",
        "Price Prediction",
        "Enter property details — area, BHK, locality, furnishing — and get an ML-powered price estimate instantly.",
        delay="0.15s",
    )
with col3:
    feature_card(
        "🤖",
        "RealtEase Assistant",
        "Ask questions about availability, pricing patterns, and listings. Optional API support for advanced chat.",
        delay="0.25s",
    )

st.markdown('<hr class="re-divider">', unsafe_allow_html=True)

section_box(
    "About this project",
    "This dashboard helps you understand Mumbai's rental market — room availability by locality, "
    "pricing trends across area, BHK, furnishing and age, plus keyword insights from listing descriptions. "
    "Use the sidebar to navigate between modules.",
)

st.markdown(
    f"""
    <div class="re-section">
        <h3>Tech Stack</h3>
        <div style="margin-top:0.75rem;">
            <span class="re-badge">Python</span>
            <span class="re-badge">Pandas & NumPy</span>
            <span class="re-badge">Scikit-Learn</span>
            <span class="re-badge">Plotly</span>
            <span class="re-badge">Matplotlib</span>
            <span class="re-badge">Streamlit</span>
            <span class="re-badge">NLTK / TF-IDF</span>
            <span class="re-badge">Random Forest</span>
        </div>
        <p style="color:#6B7C8A;margin-top:1.25rem;margin-bottom:0;font-size:0.9rem;">
            Built by <strong style="color:#4A7575;">Sumit Kanse</strong> · Academic & research use
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
