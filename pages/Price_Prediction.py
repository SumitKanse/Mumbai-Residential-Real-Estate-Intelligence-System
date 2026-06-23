import streamlit as st
import pickle
import numpy as np
import pandas as pd

from helpers.ui_theme import inject_theme, page_hero, result_card, COLORS

inject_theme()

page_hero(
    "Property Price Prediction",
    "Fill in your property details below and get an instant ML-powered price estimate "
    "trained on Mumbai real estate data.",
    badge="🔮 Machine Learning",
)

with open("model/df.pkl", "rb") as file:
    df = pickle.load(file)

with open("model/pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

st.markdown(
    f"""
    <div class="re-section" style="padding:1.25rem 1.5rem;margin-bottom:1.25rem;">
        <h3 style="margin-bottom:0.35rem;">Property Details</h3>
        <p style="margin:0;">Adjust the fields below to match the listing you're evaluating.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq. ft.)", min_value=100, step=50, value=375)
    bedroom_num = st.selectbox(
        "No. of Bedrooms",
        sorted(df["BEDROOM_NUM"].unique().tolist()),
        index=sorted(df["BEDROOM_NUM"].unique().tolist()).index(1),
    )
    balcony_num = st.selectbox(
        "No. of Balcony",
        sorted(df["BALCONY_NUM"].unique().tolist()),
        index=sorted(df["BALCONY_NUM"].unique().tolist()).index(1),
    )
    floornum = st.selectbox(
        "Floor Number",
        sorted(df["FLOOR_NUM"].unique().tolist()),
        index=sorted(df["FLOOR_NUM"].unique().tolist()).index("mid rise"),
    )

with col2:
    furnish = st.selectbox(
        "Furnishing Type",
        sorted(df["FURNISH"].unique().tolist()),
        index=sorted(df["FURNISH"].unique().tolist()).index("unfurnished"),
    )
    age = st.selectbox(
        "Age of the Property",
        sorted(df["AGE"].unique().tolist()),
        index=sorted(df["AGE"].unique().tolist()).index("10+ year old property"),
    )
    facing = st.selectbox("Facing", sorted(df["FACING"].unique().tolist()))
    locality_options = sorted(df["LOCALITY_NAME"].dropna().unique().tolist())
    locality = st.selectbox(
        "Locality Name",
        locality_options,
        index=locality_options.index("dadar"),
    )

st.markdown("<br>", unsafe_allow_html=True)
_, btn_col, _ = st.columns([1, 1.2, 1])
with btn_col:
    predict_clicked = st.button("Predict Price", use_container_width=True)

if predict_clicked:
    input_data = pd.DataFrame(
        [
            {
                "AREA": float(area),
                "BEDROOM_NUM": float(bedroom_num),
                "BALCONY_NUM": float(balcony_num),
                "FLOOR_NUM": floornum,
                "FURNISH": furnish,
                "AGE": age,
                "FACING": facing,
                "LOCALITY_NAME": locality,
            }
        ]
    )
    predicted_price = np.expm1(pipeline.predict(input_data)[0])
    result_card(predicted_price / 100_000)

    st.markdown(
        """
        <div class="re-tip">
            This is an estimate based on historical data. Market conditions, renovations,
            and location-specific factors may affect the actual price.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="re-divider">', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="re-section">
        <h3>About this model</h3>
        <p style="color:{COLORS['text_muted']};line-height:1.65;margin:0;">
            Powered by a Random Forest regressor trained on Mumbai apartment listings.
            Features include area, BHK, balcony count, floor category, furnishing,
            property age, facing direction, and locality.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
