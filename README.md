🩺 Chronic Kidney Disease Prediction using Machine Learning
📌 Project Overview

This project presents a machine learning–based system for early prediction of Chronic Kidney Disease (CKD) using clinical patient data. The system leverages the Random Forest Classifier to analyze important medical parameters and predict whether a patient is at risk of CKD.

A user-friendly Streamlit web application is developed to allow real-time predictions based on user input.

🎯 Objectives

Perform data preprocessing on CKD dataset

Build a machine learning classification model

Achieve high prediction accuracy

Deploy an interactive web interface

Assist in early screening of CKD

📂 Dataset

Source: UCI Machine Learning Repository

Dataset: Chronic Kidney Disease Dataset

Target Variable: classification (CKD / Not CKD)

✅ Selected Features

Age

Blood Pressure (bp)

Specific Gravity (sg)

Albumin (al)

Sugar (su)

⚙️ Technologies Used

Python

Pandas, NumPy

Scikit-learn

Random Forest Classifier

Streamlit

Google Colab

Ngrok

🧠 Machine Learning Model

Algorithm: Random Forest Classifier

Why Random Forest?

Handles nonlinear medical data well

Reduces overfitting

Provides high accuracy

Robust ensemble method

🔄 Project Workflow

Data Collection

Data Preprocessing

Feature Selection

Model Training

Model Evaluation

Model Saving (.pkl)

Streamlit Web App Deployment

📊 Model Performance

Accuracy: (update with your value, e.g., 98%)

Evaluation Metrics:

Accuracy Score

Confusion Matrix

🌐 Web Application

The Streamlit web app allows users to:

Enter patient clinical details

Click Predict

Instantly view CKD risk

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py
📁 Project Structure
CKD_Project/
│
├── kidney_disease.csv
├── ckd_prediction.py
├── ckd_model.pkl
├── app.py
├── README.md
└── requirements.txt
🚀 Future Scope

Use larger real-world datasets

Apply deep learning models

Add more clinical features

Deploy mobile application

Integrate with hospital systems
