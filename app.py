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

    st.image("assets/hero_banner.png", use_container_width=True)

    st.markdown("# 🏍️ Bike Rental Intelligence Dashboard")

    st.markdown(
        """
AI-Powered Bike Rental Demand Forecasting System.

Predict rental demand using weather conditions,
season, temperature, humidity and environmental factors.
"""
    )

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
