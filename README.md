# 🏡 Bengaluru House Price Prediction

This is a machine learning web application built with **Flask** that predicts house prices in **Bengaluru**, India based on input features like location, BHK, number of bathrooms, and square footage.

### 🔗 Live Demo:
👉 [Click to view the live app](https://bengaluruhousepriceprediction-o6ps.onrender.com)

---

## 📌 Features

- Predicts house prices using a trained Ridge Regression model
- Takes user input for location, BHK, bathroom count, and area
- Clean and responsive Bootstrap-based UI
- Live hosted on **Render.com**

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Flask
- **ML Model:** Scikit-learn Ridge Regression
- **Deployment:** Render.com
- **Other Tools:** Pandas, Pickle

---

## 📁 Project Structure

- `app.py` – Flask application 
- `CleanedData.csv` – Dataset used for training (required at runtime)
- `RidgeModel.pkl` – Trained ML model 
- `Procfile` – Required for Render deployment  
- `requirements.txt` – Python dependencies  
- ` templates/index.html` – Main HTML form
- `README.md` – Project documentation


## ⚙️ Installation

### 🔹 1. Clone the repository

```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

### 🔹 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Run the app

```bash
python main.py
```
The app will run on http://localhost:5001/.

## 🧠 Model Info

- Model used: Ridge Regression
- Trained on a cleaned Bengaluru housing dataset (CleanedData.csv)
- Location is one-hot encoded, and model predicts price in lakhs (₹)

## 🌐 Deployment on Render

- GitHub repo connected to Render
- Procfile and requirements.txt included
- App is automatically deployed on push
