# 💳 Customer Churn Prediction App

A sleek and interactive **Machine Learning web application** built using **Streamlit** to predict whether a customer is likely to churn based on various financial and demographic factors.

---

## 🚀 Live Demo

👉 *https://customer-churn-prediction-ann-55fy.onrender.com*

---

## 📌 Overview

Customer churn is a critical problem for businesses. This application leverages a trained **Artificial Neural Network (ANN)** model to predict the probability of a customer leaving a service.

The app provides:

* 📊 Real-time predictions
* 🎯 Probability score of churn
* 🎨 Clean and interactive UI

---

## 🧠 Model Details

* Model Type: Artificial Neural Network (ANN)
* Framework: TensorFlow / Keras
* Input Features:

  * Credit Score
  * Geography
  * Gender
  * Age
  * Tenure
  * Balance
  * Number of Products
  * Has Credit Card
  * Is Active Member
  * Estimated Salary

---

## 🖥️ Tech Stack

* **Frontend & App Framework:** Streamlit
* **Machine Learning:** TensorFlow / Keras
* **Data Processing:** Pandas, NumPy, Scikit-learn
* **Deployment:** Render

---

## 📂 Project Structure

```
customer-churn-prediction-ann/
│
├── app.py                # Main Streamlit app
├── model_fixed.h5        # Trained ANN model
├── encoder.pkl           # OneHotEncoder
├── encodegender.pkl      # LabelEncoder
├── scaler.pkl            # StandardScaler
├── requirements.txt      # Dependencies
├── runtime.txt           # Python version
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/keshavk27/Customer-churn-prediction-ANN
cd customer-churn-prediction-ann
```

---

### 2️⃣ Create virtual environment

```bash
conda create -p venv python=3.10
conda activate venv
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📊 How it works

1. User inputs customer details via sidebar
2. Data is preprocessed using saved encoders & scaler
3. Model predicts churn probability
4. Result is displayed with:

   * 📈 Progress bar
   * 📊 Probability score
   * ✅/⚠️ Decision output

---

## ✨ Features

* 🎨 Modern UI with custom styling
* ⚡ Fast real-time predictions
* 📊 Probability-based insights
* 🔍 Clean input summary display
* 💡 Beginner-friendly ML deployment

---

## ⚠️ Notes

* Model is trained on TensorFlow and optimized for deployment compatibility
* Ensure Python version is **3.10** for smooth execution
* Use `model.h5` to avoid compatibility issues

---

## 📈 Future Improvements

* 🔹 Add model explainability (SHAP/LIME)
* 🔹 Store prediction history
* 🔹 Deploy using Docker
* 🔹 Add authentication system

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Keshav**

* 💼 Aspiring ML Engineer
* 🧠 Interested in AI, Data Science, and Problem Solving

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it with others!
