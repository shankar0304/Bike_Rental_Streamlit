import streamlit as st

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="Bike Rental Intelligence Dashboard",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= LOAD CSS ================= #

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ================= SIDEBAR ================= #

st.sidebar.image("assets/logo.png", width=120)

st.sidebar.markdown("## 🏍️ Bike Rental Intelligence")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏡 Dashboard",
        "🚀 Demand Forecast",
        "📊 Analytics",
        "🧠 Model Insights",
        "📘 Documentation"
    ]
)
# ================= DASHBOARD ================= #

if page == "🏡 Dashboard":

    # ---------- HERO BANNER ---------- #

    st.image("assets/hero_banner.png", use_container_width=True)

    st.markdown(
        """
        <h1 style="font-size:55px; margin-bottom:0;">
        🏍️ Bike Rental Intelligence Dashboard
        </h1>

        <h4 style="color:#94A3B8;">
        AI Powered Demand Forecasting & Business Analytics Platform
        </h4>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # ---------- KPI CARDS ---------- #

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📊 Dataset", "17,379")

    with col2:
        st.metric("🧠 Best Model", "XGBoost")

    with col3:
        st.metric("🎯 Features", "18")

    with col4:
        st.metric("🚀 Status", "Ready")

    st.divider()

    # ---------- PROJECT OVERVIEW ---------- #

    st.markdown("## 🚀 Project Overview")

    st.write(
        """
This dashboard predicts bike rental demand using Machine Learning
and weather-based features.

The system analyzes environmental conditions, seasonal patterns,
and time-related variables to estimate expected rental demand.

It helps optimize bike availability, reduce operational costs,
and improve customer satisfaction.
"""
    )

    st.divider()

    # ---------- TECHNOLOGY STACK ---------- #

    st.markdown("## 🛠️ Technology Stack")

    tech1, tech2, tech3, tech4 = st.columns(4)

    tech1.success("🐍 Python")
    tech2.info("⚡ XGBoost")
    tech3.warning("🎈 Streamlit")
    tech4.success("🐼 Pandas")

    st.divider()

    # ---------- WORKFLOW ---------- #

    st.markdown("## 🔄 Machine Learning Workflow")

    st.markdown(
        """
📂 Dataset

⬇️

🧹 Data Cleaning

⬇️

📊 Feature Engineering

⬇️

🤖 Model Training

⬇️

🏆 XGBoost Selected

⬇️

🚀 Streamlit Deployment
"""
    )
# ================= DEMAND FORECAST ================= #

elif page == "🚀 Demand Forecast":

    st.title("🚀 Demand Forecast")

    st.write(
        "Enter the environmental and weather conditions below to predict the expected bike rental demand."
    )

    st.divider()

    # ---------- INPUT COLUMNS ---------- #

    left, right = st.columns(2)

    with left:

        season = st.selectbox(
            "Season",
            [1, 2, 3, 4]
        )

        yr = st.selectbox(
            "Year",
            [0, 1]
        )

        mnth = st.slider(
            "Month",
            1,
            12,
            6
        )

        hr = st.slider(
            "Hour",
            0,
            23,
            12
        )

        holiday = st.selectbox(
            "Holiday",
            [0, 1]
        )

        weekday = st.slider(
            "Weekday",
            0,
            6,
            3
        )

    with right:

        workingday = st.selectbox(
            "Working Day",
            [0, 1]
        )

        weathersit = st.selectbox(
            "Weather Situation",
            [1, 2, 3, 4]
        )

        temp = st.slider(
            "Temperature",
            0.0,
            1.0,
            0.50
        )

        atemp = st.slider(
            "Feels Like Temperature",
            0.0,
            1.0,
            0.50
        )

        hum = st.slider(
            "Humidity",
            0.0,
            1.0,
            0.50
        )

        windspeed = st.slider(
            "Wind Speed",
            0.0,
            1.0,
            0.20
        )

    st.divider()

    if st.button("🚀 Predict Demand", use_container_width=True):

        st.success("Prediction functionality will be connected in the next step.")

        st.metric(
            "Predicted Bike Rentals",
            "--"
        )
