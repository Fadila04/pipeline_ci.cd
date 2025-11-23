from fastapi import FastAPI
import os
import joblib
from pydantic import BaseModel

app = FastAPI()

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model", "model.pkl")

@app.get("/")
def root():
    return {"status": "OK"}


class PredictInput(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(input_data: PredictInput):
    model = joblib.load(MODEL_PATH)
    prediction = model.predict([input_data.features])
    return {"prediction": int(prediction)}

