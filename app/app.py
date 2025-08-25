import streamlit as st
import pandas as pd
import requests

df=pd.read_csv("data/Crop_recommendation.csv")

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

st.markdown("<h1 style='color: green;'> Crop Recommendation System!</h1>",unsafe_allow_html=True)

st.markdown("Let's Get the **Best Crop Recommendation:**")

st.markdown(
    """
    <style>
    .main{
        background-color: #f0fff4;/* light green background */
    }
    h1 {
        color: #2e7d32; /* dark green text */
        text-align: center;
    }
    .stButton>button{
        background-color: #4caf50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>

    """,
    unsafe_allow_html=  True
)
N = st.slider("Nitrogen (N)", min_value=int(df["N"].min()), max_value=int(df["N"].max()), value=int(df["N"].mean()))
P = st.slider("Phosphorus (P)", min_value=int(df["P"].min()), max_value=int(df["P"].max()), value=int(df["P"].mean()))
K = st.slider("Potassium (K)", min_value=int(df["K"].min()), max_value=int(df["K"].max()), value=int(df["K"].mean()))
temperature = st.slider("Temperature (°C)", min_value=float(df["temperature"].min()), max_value=float(df["temperature"].max()), value=float(df["temperature"].mean()))
humidity = st.slider("Humidity (%)", min_value=float(df["humidity"].min()), max_value=float(df["humidity"].max()), value=float(df["humidity"].mean()))
ph = st.slider("pH", min_value=float(df["ph"].min()), max_value=float(df["ph"].max()), value=float(df["ph"].mean()))
rainfall = st.slider("Rainfall (mm)", min_value=float(df["rainfall"].min()), max_value=float(df["rainfall"].max()), value=float(df["rainfall"].mean()))


if st.button("Predict Crop"):
    url = "http://127.0.0.1:8000/predict"
    payload={
        "N": N,"P": P,"K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    response=requests.post(url,json=payload)
    if response.status_code==200:
        result=response.json()
        st.subheader("🌾 Top 3 Recommended Crops:")

        cols=st.columns(3)
        for i,rec in enumerate(result["recommended_Crops"]):
            with cols[i]:
                st.markdown(
                    f"""
                    <div style="border:2px solid #4CAF50; border-radius:12px; padding:15px; text-align:center; background:#f0fff4;">
                        <h3 style="color:#2e7d32;">{rec['crop']}</h3>
                        <p><b>Confidence:</b> {rec['probability']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            

    else:
        st.error("Error Calling the API!")