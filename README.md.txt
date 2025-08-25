# 🌱 Crop Recommendation System

A Machine Learning-based web application that recommends the **top 3 crops** suitable for your soil and weather conditions. Built with **Python**, **Scikit-learn**, **FastAPI**, and **Streamlit**.

---

## Features

- Predicts crops based on **soil nutrients (N, P, K)**, **temperature**, **humidity**, **pH**, and **rainfall**.
- Returns **top 3 crop recommendations** with confidence percentages.
- Interactive **Streamlit frontend** for easy use.
- Fast **API backend** powered by **FastAPI** for real-time predictions.

---

## Folder Structure
├── api/ # FastAPI backend code
│ └── app.py
├── app/ # Streamlit frontend code
│ └── main.py
├── data/ # Dataset
│ └── Crop_recommendation.csv
├── model/ # Trained ML artifacts
│ ├── model.pkl
│ ├── scaler.pkl
│ └── encodings.pkl
├── README.md # Project documentation
├── requirements.txt # Python dependencies


