import gradio as gr
import requests
import json

API_URL = "http://localhost:5000/predict"

def predict_fraud(ssn, cc_num, first, last, gender, city, state, zip_code, city_pop, job, dob, acct_num,
                  trans_num, trans_date, trans_time, unix_time, category, amt, merchant):
    
    payload = {
        "ssn": ssn,
        "cc_num": cc_num,
        "first": first,
        "last": last,
        "gender": gender,
        "city": city,
        "state": state,
        "zip": int(zip_code),
        "city_pop": int(city_pop),
        "job": job,
        "dob": dob,
        "acct_num": acct_num,
        "trans_num": trans_num,
        "trans_date": trans_date,
        "trans_time": trans_time,
        "unix_time": int(unix_time),
        "category": category,
        "amt": float(amt),
        "merchant": merchant
    }

    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        result = response.json()
        return "Fraudulent" if result["prediction"] == 1 else "Not Fraudulent"
    else:
        return f"Error: {response.text}"

# Interface
iface = gr.Interface(
    fn=predict_fraud,
    inputs=[
        "text", "text", "text", "text", "text", "text", "text", "number", "number",
        "text", "text", "text", "text", "text", "text", "number", "text", "number", "text"
    ],
    outputs="text",
    title="Fraud Detection Predictor",
    description="Enter transaction details below to predict whether it's fraudulent.",
)

if __name__ == "__main__":
    iface.launch()
