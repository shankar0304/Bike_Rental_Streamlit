import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Bike Rental Demand Prediction",
    page_icon="🚲",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("bike_rental_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# ---------------- LOAD CSS ---------------- #

try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🚲 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home",
        "🚲 Prediction",
        "📊 EDA Dashboard",
        "📈 Model Performance",
        "ℹ️ About"
    ]
)

# ---------------- HOME PAGE ---------------- #

if page == "🏠 Home":

    st.title("🚲 Bike Rental Demand Prediction")

    st.write("""
Welcome to the Bike Rental Demand Prediction System.

This application predicts bike rental demand using weather, season,
temperature, humidity and other environmental factors.
""")

    st.success("Select a page from the sidebar to continue.")
