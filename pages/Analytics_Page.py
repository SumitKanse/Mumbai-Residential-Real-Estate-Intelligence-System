import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

from helpers.ui_theme import inject_theme, page_hero, apply_plotly_theme, COLORS, PLOTLY_LAYOUT

inject_theme()

page_hero(
    "Property Analytics",
    "Explore trends, maps, and insights across Mumbai's real estate market — "
    "drill down by locality, age, facing, and amenities.",
    badge="📊 Data Visualization",
)

map_tab, trend_tab, wordcloud_tab, sunburst_tab, radial_tab = st.tabs([
    "Map View",
    "Price Trend",
    "Amenities",
    "BHK Distribution",
    "Facing vs Price",
])


@st.cache_data
def load_group_df():
    df = pd.read_csv("data/processed/mumbai/visualization.csv")
    df["PRICE"] = round(df["PRICE"], 2)
    df["AREA"] = round(df["AREA"], 2)
    return df


@st.cache_data
def load_property_data():
    return pd.read_csv("data/mumbai/res_apartment_dataset.csv")


def clean_age(age):
    if pd.isna(age):
        return None
    age = str(age).strip().lower()
    if "under construction" in age or "new" in age:
        return 0
    if "-" in age:
        try:
            return int(age.split("-")[0])
        except ValueError:
            return None
    try:
        return int(age.split()[0])
    except (ValueError, IndexError):
        return None


group_df = load_group_df()
group_df["LOG_PRICE"] = np.log1p(group_df["PRICE"])
df = load_property_data()
df["AGE_CLEANED"] = df["AGE"].apply(clean_age)
df = df[df["PRICE"].notnull() & df["AGE_CLEANED"].notnull()]


def tab_intro(title: str, description: str):
    st.markdown(
        f"""
        <div class="re-section" style="padding:1.25rem 1.5rem;margin-bottom:1rem;">
            <h3 style="margin-bottom:0.4rem;">{title}</h3>
            <p style="margin:0;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


with map_tab:
    tab_intro(
        "Locality-wise Price & Area Map",
        "Scatter map of properties across Mumbai. Color reflects average price; marker size reflects area.",
    )
    tick_vals = list(range(14, 22))
    tick_text = [f"₹{int(np.expm1(val)) // 1_00_000}L" for val in tick_vals]
    fig = px.scatter_mapbox(
        group_df,
        lat="LATITUDE",
        lon="LONGITUDE",
        color="LOG_PRICE",
        size="AREA",
        hover_name="LOCALITY_NAME",
        hover_data={
            "PRICE": True,
            "AREA": True,
            "LOG_PRICE": False,
            "LATITUDE": False,
            "LONGITUDE": False,
        },
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        mapbox_style="open-street-map",
    )
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.update_coloraxes(
        colorbar=dict(title="AVG PRICE (₹)", tickvals=tick_vals, ticktext=tick_text)
    )
    st.plotly_chart(apply_plotly_theme(fig), use_container_width=True)

with trend_tab:
    tab_intro(
        "Price Trend by Property Age",
        "How average prices vary with building age, grouped by city — compare newer vs older stock.",
    )
    trend_df = df.groupby(["AGE_CLEANED", "CITY"])["PRICE"].mean().reset_index()
    fig2 = px.line(
        trend_df,
        x="AGE_CLEANED",
        y="PRICE",
        color="CITY",
        markers=True,
        labels={"AGE_CLEANED": "Property Age (Years)", "PRICE": "Average Price (INR)"},
        title="Average Property Price by Age Across Cities",
    )
    fig2.update_layout(legend_title_text="City")
    st.plotly_chart(apply_plotly_theme(fig2), use_container_width=True)

with wordcloud_tab:
    tab_intro(
        "Amenities Word Cloud",
        "Most frequently mentioned lifestyle features across property listings.",
    )
    amenity_keywords = [
        "gym", "swimming", "pool", "garden", "clubhouse", "security", "lift", "elevator",
        "parking", "intercom", "cctv", "wifi", "internet", "playground", "kids", "park",
        "jogging", "yoga", "indoor", "game", "sports", "fire", "alarm", "power", "backup",
        "maintenance", "community", "solar", "rainwater", "spa", "library", "theatre",
    ]
    text = " ".join(desc for desc in df["DESCRIPTION"].dropna().astype(str).str.lower())
    amenity_text = " ".join(
        word for word in re.findall(r"\b\w+\b", text) if word in amenity_keywords
    )
    wordcloud = WordCloud(
        background_color=COLORS["surface_soft"],
        colormap="GnBu",
        width=1200,
        height=600,
    ).generate(amenity_text)
    fig_wc, ax = plt.subplots(figsize=(12, 6))
    fig_wc.patch.set_facecolor(COLORS["bg"])
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig_wc)

with sunburst_tab:
    tab_intro(
        "City → Locality → BHK",
        "Hierarchical view of property availability — drill from city down to BHK configuration.",
    )
    sunburst_df = df[["CITY", "LOCALITY_NAME", "BEDROOM_NUM"]].dropna()
    sunburst_df["BHK"] = sunburst_df["BEDROOM_NUM"].astype(int).astype(str) + " BHK"
    selected_city = st.selectbox(
        "Select a city to zoom in",
        ["All Cities"] + sorted(sunburst_df["CITY"].unique()),
    )
    if selected_city != "All Cities":
        filtered_df = sunburst_df[sunburst_df["CITY"] == selected_city]
        path = ["LOCALITY_NAME", "BHK"]
    else:
        filtered_df = sunburst_df
        path = ["CITY", "LOCALITY_NAME", "BHK"]
    fig3 = px.sunburst(
        filtered_df,
        path=path,
        color_discrete_sequence=PLOTLY_LAYOUT["colorway"],
        title=f"BHK availability {'in ' + selected_city if selected_city != 'All Cities' else 'by city & locality'}",
    )
    fig3.update_layout(margin=dict(t=40, l=0, r=0, b=0))
    st.plotly_chart(apply_plotly_theme(fig3), use_container_width=True)

with radial_tab:
    tab_intro(
        "Average Price by Facing",
        "Radial comparison of average property prices across different facing directions.",
    )
    facing_df = df.groupby("FACING")["PRICE"].mean().reset_index().dropna()
    facing_df = facing_df.sort_values("PRICE", ascending=False)
    fig4 = go.Figure(
        go.Barpolar(
            r=facing_df["PRICE"],
            theta=facing_df["FACING"],
            marker_color=["#5B8E8E", "#8FB5B5", "#C9A87C", "#A8C4B8", "#7BA3A3", "#D4B896"],
            marker_line_color=COLORS["border"],
            marker_line_width=1,
            opacity=0.88,
        )
    )
    fig4.update_layout(
        title="Avg Price by Property Facing",
        polar=dict(radialaxis=dict(visible=True, gridcolor=COLORS["border"])),
        showlegend=False,
    )
    st.plotly_chart(apply_plotly_theme(fig4), use_container_width=True)
