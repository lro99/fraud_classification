import gradio as gr
import requests

def predict_fraud(**inputs):
    response = requests.post("http://flask_api:5000/predict", json=inputs)
    return "Fraud" if response.json()["prediction"] == 1 else "Not Fraud"

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
        gr.Number(label="ZIP"),
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
    outputs="text",
    title="Fraud Detection App"
)

iface.launch(server_name="0.0.0.0", server_port=7860)
