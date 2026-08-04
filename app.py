import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Bike Rental Intelligence Dashboard",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ---------------- #
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- SIDEBAR ---------------- #
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

# ---------------- DASHBOARD ---------------- #
if page == "🏡 Dashboard":

    # ---------------- HERO BANNER ---------------- #

    st.image("assets/hero_banner.png", use_container_width=True)

    st.markdown("""
    <h1 style='font-size:55px;margin-bottom:0px;'>
    🏍️ Bike Rental Intelligence Dashboard
    </h1>

    <h4 style='color:#94A3B8;margin-top:5px;'>
    AI Powered Demand Forecasting & Business Analytics Platform
    </h4>
    """, unsafe_allow_html=True)

    st.write("")

    # ---------------- KPI CARDS ---------------- #

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
    st.markdown("## 🚀 Project Overview")

st.write("""

This dashboard predicts bike rental demand using
Machine Learning and weather-based features.

The system analyzes environmental conditions,
time-related variables, and seasonal patterns
to estimate expected rental demand.

It enables business owners to optimize bike
availability, reduce operational costs,
and improve customer satisfaction.

""")
st.divider()

st.markdown("## 🛠️ Technology Stack")

c1, c2, c3, c4 = st.columns(4)

c1.success("Python")
c2.info("XGBoost")
c3.warning("Streamlit")
c4.success("Pandas")
st.divider()

st.markdown("## 🔄 Machine Learning Workflow")

st.markdown("""

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

""")

# ---------------- FORECAST ---------------- #
elif page == "🚀 Demand Forecast":

    st.title("🚀 Demand Forecast")

    st.info("Prediction page will be built next.")

# ---------------- ANALYTICS ---------------- #
elif page == "📊 Analytics":

    st.title("📊 Analytics")

    st.info("Analytics dashboard coming soon.")

# ---------------- MODEL ---------------- #
elif page == "🧠 Model Insights":

    st.title("🧠 Model Insights")

    st.info("Model comparison will be added.")

# ---------------- DOCUMENTATION ---------------- #
elif page == "📘 Documentation":

    st.title("📘 Documentation")

    st.info("Project documentation will be added.")
