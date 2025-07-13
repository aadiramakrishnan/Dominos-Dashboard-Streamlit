# 🍕 Domino’s Delivery Performance Optimization

This project analyzes factors affecting Domino’s on-time pizza delivery using predictive modeling techniques such as Logistic Regression and Random Forest. The goal is to help Domino’s enhance operational efficiency, customer satisfaction, and revenue through data-driven decisions.

## 📌 Problem Statement

Domino’s wants to understand what factors influence whether a delivery arrives on time. The dataset includes order size, weather, traffic, peak hours, delivery distance, and other operational metrics. 

**Objective**: Predict on-time delivery and identify the key drivers affecting performance.

## 🧠 Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn)
- Jupyter Notebook
- Logistic Regression, Random Forest
- Data Visualization (Matplotlib, Seaborn)
- Custom Imputation Techniques

## 🔍 Key Steps

1. **Data Cleaning**  
   - Imputed missing values in `Order Size` using derived logic:  
     `Order Size = Order Size Impact ÷ Total Dollars`
  
2. **EDA & Correlation Analysis**  
   - Assessed how delivery time, traffic, weather, etc. impact delivery performance.

3. **Hypothesis Testing & Insights**  
   - Delivery distance and peak hours have surprisingly little effect.
   - Weather and traffic degrade performance, but systems may mitigate these effects.

4. **Modeling**  
   - Logistic Regression for interpretability  
   - Random Forest for performance

5. **Evaluation Metrics**

| Metric       | Logistic Regression | Random Forest |
|--------------|---------------------|----------------|
| Accuracy     | 82.09%              | **84.77%**     |
| Precision    | 85.99%              | **88.59%**     |
| Recall       | 86.45%              | **87.82%**     |
| F1 Score     | 86.22%              | **88.20%**     |

## 💡 Business Recommendations

- **Prioritize Large & High-Value Orders**: They have the highest probability of being on-time.
- **Invest in Adverse Weather Planning**: Weather has a strong negative effect—deploy contingency routing.
- **Monitor Traffic Hotspots**: Despite low correlation, model impact suggests it's a risk factor.

## 📁 Project Files

- `dominos_model.ipynb` – Full Python notebook
- `dominos_report.pdf` – Business report version
- `README.md` – This overview

## 📈 Future Improvements

- Add live dashboard (e.g., Tableau or Streamlit)
- Deploy as API for delivery risk scoring
- Add SHAP analysis for interpretability

## 👤 Author

**Aadira Anil Ramakrishnan**  
[LinkedIn](https://www.linkedin.com/in/aadiramakrishnan/) • Data Analyst • MS in Analytics, Northeastern University

