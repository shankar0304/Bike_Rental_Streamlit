import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import joblib
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

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
# ================= LOAD DATASET ================= #

df = pd.read_csv("cleaned_dataset.csv")
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
    st.divider()

    st.markdown("## 📈 Business Insights")

    left, right = st.columns(2)

    with left:
      st.info("""
    📊 Peak rental hours:
    • 8 AM
    • 5 PM
    • 6 PM
    """)

    with right:
      st.success("""
    🌦️ Best weather:
    • Clear Sky
    • Mild Temperature
    • Low Humidity
    """)

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
         st.divider()

         st.subheader("📊 Demand Meter")

         progress = min(predicted_rentals / 1000, 1.0)

         st.progress(progress)

         st.write(f"Demand Score: **{progress*100:.1f}%**")
         st.divider() 

         st.subheader("💡 Business Recommendation")

         if predicted_rentals < 100:

             st.error("""
Low demand expected.

• Keep fewer bikes available.
• Perform maintenance during this period.
• Reduce operational costs.
""")

         elif predicted_rentals < 300:

             st.warning("""
               Moderate demand expected.

               • Maintain normal bike availability.
               • Monitor rentals regularly.
               • No major operational changes required.
               """)

         else:

         st.success("""
           High demand expected.

           • Increase bike availability.
           • Deploy extra staff.
           • Ensure all bikes are ready.
           • Great opportunity to maximize revenue.
          """)
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

    st.markdown("## 📈 Hourly Rental Trend")

    hourly = df.groupby("hr")["cnt"].mean().reset_index()

    fig = px.line(
     hourly,
     x="hr",
     y="cnt",
     markers=True,
     title="Average Bike Rentals by Hour"
    )

    fig.update_layout(
     xaxis_title="Hour of Day",
     yaxis_title="Average Rentals",
     template="plotly_dark",
     height=500
   )

    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    st.subheader("🌦️ Weather vs Bike Rentals")

    weather = df.groupby("weathersit")["cnt"].mean().reset_index()

    weather["weathersit"] = weather["weathersit"].replace({
          1: "Clear",
          2: "Mist",
          3: "Light Rain",
          4: "Heavy Rain"
   })

    fig2 = px.bar(
     weather,
     x="weathersit",
     y="cnt",
     color="cnt",
     text="cnt",
     title="Average Bike Rentals by Weather"
   )

    fig2.update_layout(
     template="plotly_dark",
     xaxis_title="Weather",
     yaxis_title="Average Rentals",
     height=500
  )

    st.plotly_chart(fig2, use_container_width=True)
    st.divider()

    st.subheader("🌡️ Temperature vs Bike Rentals")

    fig3 = px.scatter(
        df,
        x="temp",
        y="cnt",
        color="season",
        title="Temperature vs Bike Rentals",
        opacity=0.7
    )

    fig3.update_layout(
        template="plotly_dark",
        xaxis_title="Temperature",
        yaxis_title="Bike Rentals",
        height=500
    )

    st.plotly_chart(fig3, use_container_width=True)
    st.divider()

    st.subheader("📅 Monthly Rental Trend")

    monthly = df.groupby("mnth")["cnt"].mean().reset_index()

    fig4 = px.line(
        monthly,
        x="mnth",
        y="cnt",
        markers=True,
        title="Average Bike Rentals by Month"
    )

    fig4.update_layout(
        template="plotly_dark",
        xaxis_title="Month",
        yaxis_title="Average Rentals",
        height=500
    )

    st.plotly_chart(fig4, use_container_width=True)
    st.divider()

    st.subheader("💧 Humidity vs Bike Rentals")

    hum_df = df.groupby("hum")["cnt"].mean().reset_index()

    fig8 = px.line(
      hum_df,
      x="hum",
      y="cnt",
      title="Average Rentals by Humidity",
      markers=True
  )

    fig8.update_layout(
     template="plotly_dark",
     height=500
 )

    st.plotly_chart(fig8, use_container_width=True)
    st.divider()

    st.subheader("🍂 Season Distribution")

    season_data = df.groupby("season")["cnt"].sum().reset_index()

    season_data["season"] = season_data["season"].replace({
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    })

    fig5 = px.pie(
        season_data,
        names="season",
        values="cnt",
        hole=0.45,
        title="Bike Rentals by Season"
    )

    fig5.update_layout(
        template="plotly_dark",
        height=550
    )

    st.plotly_chart(fig5, use_container_width=True)
    st.divider()

    st.subheader("🔥 Correlation Heatmap")
    corr = df.corr(numeric_only=True)

    fig6 = px.imshow(
      corr,
      text_auto=True,
      aspect="auto",
      color_continuous_scale="Viridis",
      title="Feature Correlation Heatmap"
    )

    fig6.update_layout(
      template="plotly_dark",
      height=700
    )

    st.plotly_chart(fig6, use_container_width=True)

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
