# 🚌 Bus Passenger Demand Prediction – Tanzania

## 📌 Project Overview

This project develops and deploys a Machine Learning model to predict bus passenger demand based on operational and environmental factors in Tanzania.

The system helps transport companies estimate the number of passengers depending on:

- Time
- Day
- Route
- Weather
- Temperature
- Ticket Price
- Weekend Status

---

## 🎯 Objective

To design, train, evaluate, and deploy a Machine Learning model (Linear Regression and Decision Tree) that predicts passenger demand.

---

## 📊 Dataset Description

The dataset contains the following features:

| Feature | Description |
|----------|------------|
| Time | Bus departure time |
| Day | Day of the week |
| Route | Bus route |
| Weather | Weather condition |
| Temperature | Temperature in °C |
| Ticket_Price | Price of ticket |
| Is_Weekend | 0 = No, 1 = Yes |
| Passenger_Count | Number of passengers (Target variable) |

---

## 🧠 Machine Learning Models Used

1. Linear Regression
2. Decision Tree Regressor

The models were evaluated using:

- Mean Squared Error (MSE)
- R² Score

The best performing model was selected and saved as:


---

## 🚀 Deployed Application

The application was built using **Streamlit**.

It allows users to:

- Enter bus operation details
- Load the trained model
- Predict passenger demand instantly

---

## 📂 Project Files

- `ml_project.ipynb` → Model training and evaluation
- `app.py` → Streamlit application
- `model.pkl` → Trained model
- `columns.pkl` → Feature columns
- `requirements.txt` → Required libraries
- `README.md` → Project documentation

---


---

## 📈 Business Importance

This system helps:

- Transport companies manage peak hours
- Reduce overcrowding
- Improve route planning
- Increase operational efficiency

---

## 👥 Group Contribution

This project was developed collaboratively. Each member contributed to:

- Data preprocessing
- Model training
- Model evaluation
- Application development
- Deployment and documentation

---

## 📅 Submission

Course: Machine Learning Project  
Deadline: 16th February 2026  
Presentation: 18th February 2026  


