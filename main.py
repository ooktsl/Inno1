from fastapi import FastAPI
from schemas import Advertising
import joblib


app = FastAPI()

estimator_advertising_loaded = joblib.load("./randomforest_with_advertising.pkl")

def make_advertising_prediction(model, request):
    # parse input from request
    TV = request["TV"]
    Radio = request['Radio']
    Newspaper = request['Newspaper']

    # Make an input vector
    advertising = [[TV, Radio, Newspaper]]

    # Predict
    prediction = model.predict(advertising)

    return prediction[0]

# Advertising prediction endpoint
@app.post("/prediction/advertising")
def predict_advertising(request: Advertising):
    prediction = make_advertising_prediction(estimator_advertising_loaded, request.dict())
    return {"result": prediction}