# 💳 Financial Fraud Detection Pipeline

This project is an end-to-end Machine Learning and Data Engineering pipeline designed to detect fraudulent financial transactions. It was developed as the final capstone project for the **Amdocs 2nd Month Internship Program**.

The primary challenge in financial fraud detection is **extreme class imbalance** (e.g., thousands of legitimate transactions for every one fraudulent transaction). This project successfully addresses that bottleneck using robust preprocessing techniques and synthetic data generation, culminating in a highly accurate Random Forest classification model and a real-time alerting simulator.

---

## 🏗️ Architecture & Repository Structure
The project is structured as a modular, production-ready pipeline rather than a standard research notebook:

* `data/` : Contains the SQLite database and processed data files (Raw CSVs are git-ignored for security).

* `notebooks/01_EDA_and_Preprocessing.ipynb` : Handles missing values, One-Hot Encoding, `RobustScaler` for extreme outliers, and `SMOTE` for class balancing.

* `notebooks/02_Model_Training_and_Evaluation.ipynb` : Trains and evaluates Logistic Regression and Random Forest classifiers, generating performance metrics and Confusion Matrices.

* `src/database_etl.py` : An automated ETL script that extracts raw CSV data, transforms it, and loads it into a local SQLite data warehouse.

* `src/email_alert.py` : A simulated real-time alerting system using Python's `smtplib` to trigger security emails when a high-risk transaction is flagged.

* `dashboards/` : Contains the PowerBI interactive dashboard for stakeholder reporting.

---

## ⚙️ Key Technologies & Libraries
* **Language:** Python 3.13
* **Machine Learning:** Scikit-Learn (Random Forest, Logistic Regression)
* **Data Balancing:** Imbalanced-Learn (SMOTE)
* **Data Manipulation:** Pandas, NumPy
* **Data Engineering:** SQLite3
* **Visualization:** Seaborn, Matplotlib, PowerBI

---

## 📊 Business Impact
By prioritizing the **Recall** metric alongside the ROC-AUC score, this pipeline is optimized to minimize False Negatives. In a real-world financial context, missing a fraudulent transaction (False Negative) is significantly more expensive than temporarily flagging a legitimate transaction (False Positive).
