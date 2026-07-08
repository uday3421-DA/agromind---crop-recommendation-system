# 🌾 AgroMind – Crop Recommendation System

AgroMind is a Machine Learning-powered Crop Recommendation System that helps farmers identify the most suitable crop based on soil nutrients and environmental conditions. The application is built using **Python**, **Scikit-learn**, and **Streamlit** with an interactive user interface.

---

## 📌 Project Overview

Choosing the right crop is one of the most important decisions in agriculture. This project predicts the best crop to cultivate using Machine Learning by analyzing:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

The model recommends the most suitable crop while also validating unrealistic input values and providing helpful warnings.

---

## 🚀 Features

- 🌱 Machine Learning based crop prediction
- 🎯 High prediction accuracy using trained classification model
- 📊 Interactive Streamlit web application
- ✅ Input validation for soil and weather values
- ⚠️ Crop-specific environmental warnings
- 📋 Displays user input summary before prediction
- 🎈 Success animation after successful prediction
- 💻 Simple and user-friendly interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Scikit-learn | Machine Learning |
| NumPy | Numerical Computation |
| Pickle | Model Serialization |
| Pandas | Data Processing |
| Jupyter Notebook | Model Training |

---

## 📂 Project Structure

```
AgroMind/
│
├── app.py                         # Streamlit Application
├── crop_model.pkl                 # Trained Machine Learning Model
├── Crop_recommendation.csv        # Dataset
├── training_testing_data.ipynb    # Model Training Notebook
├── requirements.txt
├── README.md
└── screenshots/
      ├── home.png
      └── prediction.png
```

---

## 📈 Input Parameters

The model uses the following seven parameters:

| Feature | Description |
|----------|-------------|
| Nitrogen | Soil Nitrogen Content |
| Phosphorus | Soil Phosphorus Content |
| Potassium | Soil Potassium Content |
| Temperature | Temperature (°C) |
| Humidity | Relative Humidity (%) |
| pH | Soil pH Value |
| Rainfall | Rainfall (mm) |

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Model Serialization using Pickle
7. Deployment using Streamlit

---

## 🖥️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AgroMind.git
```

```bash
cd AgroMind
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📸 Application Preview

### Home Page

- Enter soil nutrient values
- Enter weather details
- Click **Recommend Crop**

### Prediction

The application predicts the most suitable crop and provides:

- Recommended crop
- Input validation
- Environmental warnings (if required)

---

## 📊 Dataset

The project uses a crop recommendation dataset containing multiple crop categories with soil and weather attributes.

Dataset Features:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall
- Crop Label

---

## 👨‍💻 Author

**Uday Gaikwad**

Artificial Intelligence & Data Science Student

## ⭐ If you like this project

Give this repository a ⭐ and feel free to contribute.

---

## 📜 License

This project is developed for educational and learning purposes.
