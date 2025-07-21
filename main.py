# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI(
    title="Heart Failure Risk Prediction API",
    description="Predicts heart failure risk using clinical features.",
    version="1.0"
)

# Load model and scaler
model = joblib.load('C:/Users/ABHIRAM/projects/code/model.pkl')
scaler = joblib.load('C:/Users/ABHIRAM/projects/code/scaler.pkl')

# Define the input format
class PatientData(BaseModel):
    age: float
    anaemia: int
    creatinine_phosphokinase: float
    diabetes: int
    ejection_fraction: float
    high_blood_pressure: int
    platelets: float
    serum_creatinine: float
    serum_sodium: float
    sex: int
    smoking: int
    time: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Heart Failure Risk Prediction API"}

@app.post("/predict/")
def predict(data: PatientData):
    try:
        features = [
            data.age, data.anaemia, data.creatinine_phosphokinase, data.diabetes,
            data.ejection_fraction, data.high_blood_pressure, data.platelets,
            data.serum_creatinine, data.serum_sodium, data.sex, data.smoking, data.time
        ]
        scaled = scaler.transform([features])
        prediction = model.predict(scaled)[0]

        result = "High Risk of Heart Failure" if prediction == 1 else "Low Risk of Heart Failure"
        return {"prediction": int(prediction), "result": result}

    except Exception as e:
        return {"error": str(e)}
