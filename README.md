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
project/
|-- api/ # Backend (FastAPI for serving ML model)
| -- app.py |-- app/ # Frontend (Streamlit app for UI) | -- main.py
|-- data/ # Raw dataset
| -- Crop_recommendation.csv |-- model/ # Trained machine learning models | |-- model.pkl | |-- scaler.pkl | -- encodings.pkl
|-- README.md # Documentation
`-- requirements.txt # Dependencies
