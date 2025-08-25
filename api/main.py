import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model=joblib.load("model.pkl")
le=joblib.load("encodings.pkl")
scaler=joblib.load("scaler.pkl")

app=FastAPI()

class name_type(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.get("/")
def home():
    return {"message": "Crop Recommendation API is Running>>>>"}

@app.post("/predict")
def predict_Crop(data: name_type):
    input_df=pd.DataFrame([[data.N,data.P,data.K,data.temperature,data.humidity,data.ph,data.rainfall]],
                          columns=["N","P","K","temperature","humidity","ph","rainfall"])
    
    input_scaler=scaler.transform(input_df)
    
    probs=model.predict_proba(input_scaler)[0]
    top3_idx=np.argsort(probs)[-3:][::-1]
    top3_crop=le.inverse_transform(top3_idx)
    top3_prob=probs[top3_idx]
    return {
        "recommended_Crops": [
            {"crop": crop, "probability": f"{prob*100:.2f}%"}
            for crop,prob in zip(top3_crop,top3_prob)
        ]
    }
