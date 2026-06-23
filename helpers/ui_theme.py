"""Shared UI theme — soothing palette, animations, and layout helpers."""

import streamlit as st

# Soothing palette
COLORS = {
    "bg": "#F7F5F1",
    "surface": "#FFFFFF",
    "surface_soft": "#F0EDE8",
    "primary": "#5B8E8E",
    "primary_dark": "#4A7575",
    "primary_light": "#8FB5B5",
    "accent": "#C9A87C",
    "accent_soft": "#EDE4D8",
    "text": "#2C3E50",
    "text_muted": "#6B7C8A",
    "border": "#E2DDD6",
    "success": "#6B9E78",
    "shadow": "rgba(44, 62, 80, 0.08)",
}

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color=COLORS["text"], size=13),
    colorway=["#5B8E8E", "#C9A87C", "#8FB5B5", "#A8C4B8", "#D4B896", "#7BA3A3"],
    margin=dict(l=40, r=24, t=48, b=40),
)


def inject_theme():
    """Inject global CSS for the entire app."""
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

        html, body, [class*="css"] {{
            font-family: 'DM Sans', sans-serif !important;
        }}

        .stApp {{
            background: linear-gradient(165deg, {COLORS['bg']} 0%, #EDE9E3 45%, {COLORS['bg']} 100%);
            color: {COLORS['text']};
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #FFFFFF 0%, {COLORS['surface_soft']} 100%);
            border-right: 1px solid {COLORS['border']};
        }}
        section[data-testid="stSidebar"] .stMarkdown h1,
        section[data-testid="stSidebar"] .stMarkdown h2,
        section[data-testid="stSidebar"] .stMarkdown h3 {{
            color: {COLORS['primary_dark']} !important;
            font-weight: 600;
        }}
        [data-testid="stSidebarNav"] a {{
            border-radius: 10px !important;
            padding: 0.55rem 0.75rem !important;
            margin: 2px 0 !important;
            transition: all 0.25s ease !important;
            color: {COLORS['text']} !important;
        }}
        [data-testid="stSidebarNav"] a:hover {{
            background: {COLORS['accent_soft']} !important;
            transform: translateX(4px);
        }}
        [data-testid="stSidebarNav"] a[aria-selected="true"] {{
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['primary_dark']} 100%) !important;
            color: white !important;
            font-weight: 600;
            box-shadow: 0 4px 14px {COLORS['shadow']};
        }}

        /* Headings */
        h1, h2, h3, h4 {{
            color: {COLORS['text']} !important;
            letter-spacing: -0.02em;
        }}
        h1 {{
            font-weight: 700 !important;
            background: linear-gradient(135deg, {COLORS['primary_dark']} 0%, {COLORS['primary']} 60%, {COLORS['accent']} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background: {COLORS['surface_soft']};
            border-radius: 14px;
            padding: 6px;
            border: 1px solid {COLORS['border']};
        }}
        .stTabs [data-baseweb="tab"] {{
            border-radius: 10px !important;
            padding: 0.6rem 1.1rem !important;
            font-weight: 500 !important;
            color: {COLORS['text_muted']} !important;
            background: transparent !important;
            transition: all 0.3s ease !important;
        }}
        .stTabs [data-baseweb="tab"]:hover {{
            color: {COLORS['primary']} !important;
            background: rgba(255,255,255,0.7) !important;
        }}
        .stTabs [aria-selected="true"] {{
            background: {COLORS['surface']} !important;
            color: {COLORS['primary_dark']} !important;
            font-weight: 600 !important;
            box-shadow: 0 2px 10px {COLORS['shadow']};
        }}
        .stTabs [data-baseweb="tab-panel"] {{
            padding-top: 1.25rem;
            animation: fadeSlideIn 0.45s ease-out;
        }}

        /* Buttons */
        .stButton > button {{
            background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['primary_dark']} 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.55rem 1.4rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 14px rgba(91, 142, 142, 0.25);
        }}
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 22px rgba(91, 142, 142, 0.35) !important;
        }}
        .stButton > button:active {{
            transform: translateY(0);
        }}

        /* Inputs */
        .stNumberInput input, .stTextInput input, .stSelectbox > div > div,
        [data-baseweb="select"] > div {{
            border-radius: 10px !important;
            border-color: {COLORS['border']} !important;
            transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
        }}
        .stNumberInput input:focus, .stTextInput input:focus {{
            border-color: {COLORS['primary']} !important;
            box-shadow: 0 0 0 3px rgba(91, 142, 142, 0.15) !important;
        }}

        /* Chat */
        [data-testid="stChatMessage"] {{
            border-radius: 14px !important;
            border: 1px solid {COLORS['border']};
            background: {COLORS['surface']} !important;
            animation: fadeSlideIn 0.4s ease-out;
            margin-bottom: 0.75rem;
        }}
        [data-testid="stChatInput"] {{
            border-radius: 14px !important;
        }}

        /* Dataframes & metrics */
        [data-testid="stDataFrame"] {{
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid {COLORS['border']};
        }}
        [data-testid="stMetric"] {{
            background: {COLORS['surface']};
            border-radius: 12px;
            padding: 1rem;
            border: 1px solid {COLORS['border']};
            box-shadow: 0 2px 12px {COLORS['shadow']};
            animation: fadeSlideIn 0.5s ease-out;
        }}

        /* Plotly charts */
        .js-plotly-plot {{
            border-radius: 14px;
            overflow: hidden;
            border: 1px solid {COLORS['border']};
            background: {COLORS['surface']};
            box-shadow: 0 4px 20px {COLORS['shadow']};
            animation: fadeSlideIn 0.55s ease-out;
        }}

        /* Spinner */
        .stSpinner > div {{
            border-top-color: {COLORS['primary']} !important;
        }}

        /* Hide default Streamlit chrome for cleaner look */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header[data-testid="stHeader"] {{
            background: rgba(247, 245, 241, 0.85);
            backdrop-filter: blur(8px);
        }}

        /* Custom component classes */
        .re-hero {{
            background: linear-gradient(135deg, {COLORS['primary_dark']} 0%, {COLORS['primary']} 50%, #7BA8A8 100%);
            border-radius: 20px;
            padding: 2.5rem 2rem;
            color: white;
            margin-bottom: 1.75rem;
            box-shadow: 0 12px 40px rgba(74, 117, 117, 0.28);
            animation: fadeSlideIn 0.6s ease-out;
            position: relative;
            overflow: hidden;
        }}
        .re-hero::after {{
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 60%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%);
            pointer-events: none;
        }}
        .re-hero h1 {{
            -webkit-text-fill-color: white !important;
            color: white !important;
            background: none !important;
            font-size: 2rem;
            margin: 0 0 0.5rem 0;
            position: relative;
        }}
        .re-hero p {{
            color: rgba(255,255,255,0.92);
            font-size: 1.05rem;
            line-height: 1.6;
            margin: 0;
            max-width: 680px;
            position: relative;
        }}

        .re-card {{
            background: {COLORS['surface']};
            border: 1px solid {COLORS['border']};
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px {COLORS['shadow']};
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeSlideIn 0.5s ease-out backwards;
            height: 100%;
        }}
        .re-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(44, 62, 80, 0.12);
        }}
        .re-card-icon {{
            font-size: 2rem;
            margin-bottom: 0.75rem;
            display: block;
        }}
        .re-card h3 {{
            color: {COLORS['primary_dark']} !important;
            font-size: 1.15rem;
            margin: 0 0 0.5rem 0;
        }}
        .re-card p {{
            color: {COLORS['text_muted']};
            font-size: 0.92rem;
            line-height: 1.55;
            margin: 0;
        }}

        .re-section {{
            background: {COLORS['surface']};
            border: 1px solid {COLORS['border']};
            border-radius: 16px;
            padding: 1.75rem;
            margin: 1rem 0 1.5rem 0;
            box-shadow: 0 4px 18px {COLORS['shadow']};
            animation: fadeSlideIn 0.45s ease-out;
        }}
        .re-section h2, .re-section h3 {{
            color: {COLORS['primary_dark']} !important;
            margin-top: 0;
        }}

        .re-badge {{
            display: inline-block;
            background: {COLORS['accent_soft']};
            color: {COLORS['primary_dark']};
            padding: 0.35rem 0.85rem;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 500;
            margin: 0.25rem;
            border: 1px solid {COLORS['border']};
            transition: all 0.25s ease;
        }}
        .re-badge:hover {{
            background: {COLORS['primary_light']};
            color: white;
            transform: scale(1.04);
        }}

        .re-result {{
            background: linear-gradient(135deg, #E8F4F0 0%, #F0EDE8 100%);
            border: 1px solid {COLORS['primary_light']};
            border-radius: 16px;
            padding: 1.5rem 2rem;
            text-align: center;
            animation: popIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            margin: 1.25rem 0;
        }}
        .re-result .price {{
            font-size: 2rem;
            font-weight: 700;
            color: {COLORS['primary_dark']};
            margin: 0.25rem 0;
        }}
        .re-result .label {{
            color: {COLORS['text_muted']};
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }}

        .re-tip {{
            background: {COLORS['accent_soft']};
            border-left: 4px solid {COLORS['accent']};
            border-radius: 0 12px 12px 0;
            padding: 1rem 1.25rem;
            color: {COLORS['text_muted']};
            font-size: 0.9rem;
            line-height: 1.6;
            margin: 1rem 0;
        }}

        .re-divider {{
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, {COLORS['border']}, transparent);
            margin: 2rem 0;
        }}

        @keyframes fadeSlideIn {{
            from {{ opacity: 0; transform: translateY(14px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes popIn {{
            from {{ opacity: 0; transform: scale(0.92); }}
            to   {{ opacity: 1; transform: scale(1); }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_hero(title: str, subtitle: str, badge: str = ""):
    badge_html = f'<span style="opacity:0.85;font-size:0.85rem;">{badge}</span><br>' if badge else ""
    st.markdown(
        f"""
        <div class="re-hero">
            {badge_html}
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def feature_card(icon: str, title: str, description: str, delay: str = "0s"):
    st.markdown(
        f"""
        <div class="re-card" style="animation-delay: {delay};">
            <span class="re-card-icon">{icon}</span>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_box(title: str, content: str, level: int = 3):
    tag = f"h{level}"
    st.markdown(
        f"""
        <div class="re-section">
            <{tag}>{title}</{tag}>
            <p style="color:{COLORS['text_muted']};line-height:1.65;margin-bottom:0;">{content}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def result_card(price_lacs: float):
    st.markdown(
        f"""
        <div class="re-result">
            <div class="label">Estimated Property Price</div>
            <div class="price">₹ {price_lacs:,.2f} Lacs</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def apply_plotly_theme(fig):
    fig.update_layout(**PLOTLY_LAYOUT)
    return fig
