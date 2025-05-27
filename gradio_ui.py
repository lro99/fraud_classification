import gradio as gr
import requests

def predict_fraud(ssn, cc_num, first, last, gender, city, state, zip_code, city_pop, job, dob, acct_num, trans_num, trans_date, trans_time, unix_time, category, amt, merchant):

    url = "http://flask_api:5000/predict"
    payload = {
        "ssn": ssn,
        "cc_num": cc_num,
        "first": first,
        "last": last,
        "gender": gender,
        "city": city,
        "state": state,
        "zip": zip_code,
        "city_pop": city_pop,
        "job": job,
        "dob": dob,
        "acct_num", acct_num,
        "trans_num", trans_num,
        "trans_date", trans_date,
        "trans_time", trans_time,
        "unix_time", unix_time,
        "category", category,
        "amt", amt,
        "merchant", merchant
    }

    try:
        response = requests.post(url, json=payload)
        result = response.json()
        return f"Prediction: {'FRAUD' if result['prediction'] == 1 else 'NOT FRAUD'}"
    except Exception as e:
        return f"Error: {e}"

# Gradio interface
iface = gr.Interface(
    fn=predict_fraud,
    inputs=[
        gr.Textbox(label="SSN"),
        gr.Textbox(label="CC Num"),
        gr.Textbox(label="First Name"),
        gr.Textbox(label="Last Name"),
        gr.Dropdown(["M", "F"], label="Gender"),
        gr.Textbox(label="City"),
        gr.Textbox(label="State"),
        gr.Number(label="ZIP Code"),
        gr.Number(label="City Population"),
        gr.Textbox(label="Job"),
        gr.Textbox(label="Date of Birth"),
        gr.Textbox(label="Account Number"),
        gr.Textbox(label="Transaction Number"),
        gr.Textbox(label="Transaction Date (YYYY-MM-DD)"),
        gr.Textbox(label="Transaction Time (HH:MM:SS)"),
        gr.Number(label="Unix Time"),
        gr.Textbox(label="Category"),
        gr.Number(label="Amount"),
        gr.Textbox(label="Merchant")
    ],
    outputs=gr.Text(label="Prediction"),
    title="Fraud Detection App"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
