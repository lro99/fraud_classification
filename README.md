# fraud_classification

# 💳 Credit Card Fraud Detection with TensorFlow

This project builds a machine learning model using TensorFlow to detect fraudulent credit card transactions. It tackles the common challenge of highly imbalanced datasets and aims to prioritize **recall** to reduce overlooked fraudulent activity.

---

## 📌 Project Overview

Financial fraud, especially credit card fraud, is a serious issue costing billions annually. This model classifies transactions as either **fraudulent** or **legitimate** using machine learning.

Key highlights:
- Built using **TensorFlow** and **Keras**
- Handles **imbalanced data** (fraudulent transactions ~0.36%)
- Focuses on **recall** to reduce false negatives
- Includes preprocessing, model training, evaluation, and visualization

---

## 📂 Dataset

- **Source:** [Kaggle Credit Card Fraud Detection Dataset](https://huggingface.co/datasets/Nooha/cc_fraud_detection_dataset/tree/main/data)
- Features:
  - 2,646,694 transactions
  - 9,422 fraudulent cases (~0.36%)

---

## 🧠 Model Architecture

- Input Layer: 15 features
- Hidden Layers: Fully connected (`Dense`) layers with ReLU activations
- Dropout regularization to prevent overfitting
- Output Layer: Single neuron with sigmoid activation for binary classification

---
