
# 🍕 Domino’s Delivery Performance Optimization – ML + Dashboard

> 📊 Live Dashboard: [Launch the App](https://dominos-dashboard-app-ray9ctnwrz9ka5xbm4fves.streamlit.app/)  
> 🧠 Project Type: End-to-End Data Science | ML Modeling | Streamlit Dashboard | Real-World Analysis

---

## 🧩 Project Overview

This project aims to predict on-time delivery for Domino’s orders using machine learning and uncover the key drivers that influence delivery success. The solution includes an interactive **Streamlit dashboard**, model-driven insights, and post-launch performance analysis — even when the results were unexpected.

---

## 🚀 Why This Project Matters

**On-time delivery is critical** for customer satisfaction, revenue, and brand loyalty in food delivery. This project tackles:
- Predicting whether an order will be delivered on time
- Understanding which factors (weather, order size, traffic) drive that outcome
- Comparing pre-test vs post-test performance to evaluate real business impact

---

## 🛠️ Tech Stack

| Layer        | Tools & Libraries                        |
|--------------|-------------------------------------------|
| Data         | CSV (Dominos_Full_Example.csv)            |
| Modeling     | Python, Pandas, Scikit-learn, RandomForest, LogisticRegression |
| Dashboard    | Streamlit, Plotly, Statsmodels            |
| Visualization| Plotly Express, Graph Objects             |
| Deployment   | Streamlit Cloud                           |

---

## 📊 Key Features in the Dashboard

🔗 **[Launch Dashboard](https://dominos-dashboard-app-ray9ctnwrz9ka5xbm4fves.streamlit.app/)**  

The live dashboard includes:

- ✅ Pre vs Post Test on-time delivery comparison
- ✅ Actual vs Predicted delivery performance by test phase
- ✅ Model accuracy + business metrics
- ✅ Correlation matrix and variable impact (Order Size, Weather, Distance)
- ✅ Store-location and order-type performance heatmaps
- ✅ Dynamic filters (Test Phase, Store, Order Type)

---

## 🧠 Modeling Summary

Two models were trained:
- **Logistic Regression** for interpretability  
- **Random Forest** for performance

| Metric       | Logistic Regression | Random Forest |
|--------------|---------------------|----------------|
| Accuracy     | 82.09%              | **84.77%**     |
| Precision    | 85.99%              | **88.59%**     |
| Recall       | 86.45%              | **87.82%**     |
| F1 Score     | 86.22%              | **88.20%**     |

📌 **Key Drivers Identified by the Model**:
- High impact: **Order Size**, **Total Dollars**
- Negative impact: **Weather**, **Traffic**
- Unexpected insight: **Distance & Peak Hours had minimal effect**

---

## ❗ Unexpected Outcome: What Happened Post-Test?

Despite strong model performance, the **real-world post-test delivery performance dropped by 31.3%**.

### 📉 Insight from the Dashboard:
- On-time delivery rate **fell from ~50% to ~18%**
- This was visualized clearly in the dashboard, with metric cards and comparison charts

### 🔎 Diagnosis:
- The model predicted well on validation data but **did not translate into business improvement**
- Possible causes:
  - External disruptions (e.g., weather, staffing, volume spike)
  - Poor operational execution of the model insights
  - Data drift or mismatch between pre-test and post-test conditions

### 🎓 What This Shows:
> A model can be statistically strong, but if **not implemented well**, the real-world impact can still fail.  
> This project shows not just ML skill — but the ability to **diagnose performance gaps** through dashboards and business thinking.

---

## ✅ Business Recommendations

- Prioritize high-value, high-complexity orders (they’re more likely to be on time)
- Re-evaluate the operational rollout plan post-model deployment
- Investigate weather and traffic effects further — consider real-time route planning
- Monitor model vs actual results continuously via dashboards

---

## 📂 Files in This Project

```
dominos-delivery-performance/
├── dominos_dashboard.py          # Streamlit dashboard code
├── dominos_model.ipynb           # Modeling + EDA notebook
├── Dominos_Full_Example.csv      # Dataset
├── dominos_report.pdf            # Business-style project report
├── requirements.txt              # For deployment
├── README.md                     # You're reading this!
```

---

## 🧑‍💼 Author

**Aadira Anil Ramakrishnan**  
MS in Analytics, Northeastern University  
[LinkedIn](https://www.linkedin.com/in/aadiramakrishnan/)  

---

## 📄 License

MIT License. See `LICENSE` file for details.


