import os
import streamlit as st
import geopandas as gpd
from sqlalchemy import create_engine
import folium
from streamlit_folium import st_folium
from datetime import datetime
from dotenv import load_dotenv

# =========================
# LOAD ENVIRONMENT VARIABLES
# =========================

load_dotenv()

# =========================
# PAGE CONFIG — must be first st call
# =========================

st.set_page_config(
    page_title="Lahore AQI Dashboard",
    page_icon="🌫️",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>
    .block-container { padding-top: 2rem; }
    [data-testid="metric-container"] {
        background-color: #808080;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 1rem;
    }
    .aqi-good    { background:#d4edda; color:#155724; padding:4px 12px; border-radius:8px; font-size:13px; }
    .aqi-fair    { background:#fff3cd; color:#856404; padding:4px 12px; border-radius:8px; font-size:13px; }
    .aqi-moderate{ background:#fde8d8; color:#7d3c0a; padding:4px 12px; border-radius:8px; font-size:13px; }
    .aqi-poor    { background:#f8d7da; color:#721c24; padding:4px 12px; border-radius:8px; font-size:13px; }
    .aqi-verypoor{ background:#e2bfca; color:#4a0018; padding:4px 12px; border-radius:8px; font-size:13px; }
</style>
""", unsafe_allow_html=True)

# =========================
# DATABASE CONNECTION
# =========================

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ... rest of your dashboard.py stays exactly the same