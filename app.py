import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import pandas as pd
import numpy as np

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
# ================= LOAD MODEL ================= #

model = joblib.load("bike_rental_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# ================= SIDEBAR ================= #
# ================= TOP NAVIGATION ================= #

col1, col2 = st.columns([1,8])

with col1:
    st.image("assets/logo.png", width=65)

with col2:
    st.markdown("""
    <h1 style="
    color:white;
    margin-top:8px;
    font-size:42px;
    font-weight:700;
    ">
    🏍️ Bike Rental Intelligence
    </h1>
    """, unsafe_allow_html=True)
selected = option_menu(
    menu_title=None,
    options=[
        "Dashboard",
        "Forecast",
        "Analytics",
        "Model",
        "Docs"
    ],
    icons=[
        "house-fill",
        "rocket-fill",
        "bar-chart-fill",
        "cpu-fill",
        "book-fill"
    ],
    orientation="horizontal",
    default_index=0,

    styles={
        "container": {
            "padding": "8px",
            "background-color": "#1E293B",
            "border-radius": "18px"
        },
        "icon": {
            "color": "#38BDF8",
            "font-size": "18px"
        },
        "nav-link": {
            "font-size": "17px",
            "color": "white",
            "text-align": "center",
            "margin": "5px",
            "border-radius": "12px",
        },
        "nav-link-selected": {
            "background-color": "#2563EB",
        },
    }
)

st.divider()
# ================= DASHBOARD ================= #

if selected == "Dashboard":

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
        # ---------- KPI CARDS ---------- #

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">📊 Dataset</div>
            <div class="metric-value">17,379</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">🧠 Best Model</div>
            <div class="metric-value">XGBoost</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">🎯 Features</div>
            <div class="metric-value">18</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">🚀 Status</div>
            <div class="metric-value">Ready</div>
        </div>
        """, unsafe_allow_html=True)

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

elif selected == "Forecast":

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

         input_data = pd.DataFrame({
            "season": [season],
            "yr": [yr],
            "mnth": [mnth],
            "hr": [hr],
            "holiday": [holiday],
            "weekday": [weekday],
            "workingday": [workingday],
            "weathersit": [weathersit],
            "temp": [temp],
            "atemp": [atemp],
            "hum": [hum],
            "windspeed": [windspeed]
         })

         st.subheader("Input Data")

         st.dataframe(input_data)
           # Reorder columns
         input_data = input_data.reindex(columns=feature_columns)
 
         st.subheader("Reordered Data")
         st.dataframe(input_data)

         # Scale the input
         scaled_input = scaler.transform(input_data)
 
         # Predict
         prediction = model.predict(scaled_input)

         predicted_rentals = int(prediction[0])

         st.divider()

         # Decide demand level
         if predicted_rentals < 100:
            demand = "🔴 LOW DEMAND"
            color = "#EF4444"

         elif predicted_rentals < 300:
              demand = "🟡 MEDIUM DEMAND"
              color = "#FACC15"

         else:
             demand = "🟢 HIGH DEMAND"
             color = "#22C55E"

         # Premium Prediction Card
         st.markdown(f"""
         <div style="
         background:#1E293B;
         padding:30px;
         border-radius:20px;
         text-align:center;
         border:2px solid #38BDF8;
         margin-top:20px;
         ">

         <h4 style="color:#94A3B8;">
         🏍️ Predicted Bike Rental Demand
         </h4>

         <h1 style="
         font-size:60px;
         color:#38BDF8;
         margin:10px 0;
         ">
         {predicted_rentals}
         </h1>

         <h3 style="color:white;">
         Expected Rentals
         </h3>

         </div>
         """, unsafe_allow_html=True)

         # Demand Status Card
         st.markdown(f"""
         <div style="
         background:{color};
         padding:18px;
         border-radius:15px;
         text-align:center;
         font-size:24px;
         font-weight:bold;
         color:white;
         margin-top:20px;
         ">
         {demand}
         </div>
         """, unsafe_allow_html=True)
    # ---------- KPI CARDS ---------- #

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric("📊 Total Records", "17,379")

    with kpi2:
        st.metric("🎯 Features", "18")

    with kpi3:
        st.metric("🧠 Best Model", "XGBoost")

    with kpi4:
        st.metric("📈 Status", "Ready")

    st.divider()

    st.markdown("## 📈 Analytics Available")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📅 Hourly Rental Analysis")
        st.info("🌦️ Weather Impact")
        st.info("🍂 Seasonal Demand")

    with col2:
        st.info("🔥 Correlation Heatmap")
        st.info("📊 Feature Distribution")
        st.info("📉 Rental Trends")

    st.divider()

    st.success(
        "Interactive Plotly charts will be added in the next phase."
    )
    # ================= ANALYTICS ================= #

elif selected == "Analytics":

    st.title("📊 Data Analytics Dashboard")

    st.write(
        "Explore key insights and visualizations from the Bike Rental dataset."
    )

    st.divider()

    # KPI Cards
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric("📊 Total Records", "17,379")

    with kpi2:
        st.metric("🎯 Features", "18")

    with kpi3:
        st.metric("🧠 Best Model", "XGBoost")

    with kpi4:
        st.metric("📈 Status", "Ready")

    st.divider()

    st.subheader("📈 Analytics Available")

    col1, col2 = st.columns(2)

    with col1:
        st.success("📅 Hourly Rental Analysis")
        st.success("🌦️ Weather Impact")
        st.success("🍂 Seasonal Demand")

    with col2:
        st.info("🔥 Correlation Heatmap")
        st.info("📊 Feature Distribution")
        st.info("📉 Rental Trends")

    st.divider()

    st.info("Interactive charts will be added later.")
    # ================= MODEL INSIGHTS ================= #

elif selected == "Model":

    st.title("🧠 Model Insights")

    st.write(
        "Performance summary of the machine learning models used for bike rental demand prediction."
    )

    st.divider()

    st.markdown("## 🏆 Best Model")

    st.success("✅ XGBoost was selected as the best-performing model.")

    st.divider()

    st.markdown("## 📊 Model Comparison")

    model_data = {
        "Model": [
            "Linear Regression",
            "Decision Tree",
            "Random Forest",
            "XGBoost"
        ],
        "Status": [
            "Baseline",
            "Good",
            "Very Good",
            "Best Model ✅"
        ]
    }

    st.table(model_data)

    st.divider()

    st.markdown("## ⭐ Why XGBoost?")

    st.markdown("""
- High prediction accuracy
- Handles nonlinear relationships
- Reduces overfitting
- Fast and efficient
- Suitable for structured tabular datasets
""")

    st.divider()

    st.info("📌 Feature Importance chart will be added in the next phase.")
    # ================= DOCUMENTATION ================= #

elif selected == "Docs":

    st.title("📘 Project Documentation")

    st.divider()

    st.markdown("## 🎯 Problem Statement")

    st.write("""
Predict the number of bike rentals based on weather,
season, temperature, humidity, and time-related features.
""")

    st.divider()

    st.markdown("## 📂 Dataset")

    st.write("""
Dataset: Bike Sharing Demand Dataset

Records: 17,379

Target Variable:
• Bike Rental Count
""")

    st.divider()

    st.markdown("## ⚙️ Machine Learning Pipeline")

    st.markdown("""
1. Data Cleaning

2. Exploratory Data Analysis

3. Feature Engineering

4. Model Training

5. Model Evaluation

6. XGBoost Model Selection

7. Streamlit Deployment
""")

    st.divider()

    st.success("🚀 Developed using Python, XGBoost and Streamlit.")
