# Heart_Disease-prediction
# Heart Failure Risk Prediction API

This project is a machine learning-powered web API built using **Python** and **FastAPI** that predicts whether a person is at risk of heart failure based on clinical features.

## Features

- Predicts the risk of heart failure as "High Risk" or "Low Risk"
- Built using a trained **Random Forest Classifier**
- Uses a **StandardScaler** for preprocessing
- Developed using **FastAPI** for efficient and fast deployment
- Interactive API documentation available at `/docs`

## Dataset

The model is trained on the [Heart Failure Clinical Records Dataset](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data), which contains 12 input clinical features and a target variable indicating mortality.

## Input Features

- `age`: Age of the patient
- `anaemia`: 1 if the patient has anaemia; otherwise 0
- `creatinine_phosphokinase`: Level of CPK enzyme in the blood
- `diabetes`: 1 if the patient has diabetes; otherwise 0
- `ejection_fraction`: Percentage of blood leaving the heart at each contraction
- `high_blood_pressure`: 1 if the patient has hypertension; otherwise 0
- `platelets`: Platelet count in the blood
- `serum_creatinine`: Level of creatinine in the blood
- `serum_sodium`: Level of sodium in the blood
- `sex`: 1 for male, 0 for female
- `smoking`: 1 if the patient smokes; otherwise 0
- `time`: Follow-up period (in days)

## Setup Instructions

1. **Clone the repository** (if applicable) and navigate to the project folder.

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
