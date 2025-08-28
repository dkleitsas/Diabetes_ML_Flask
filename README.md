# Pima Diabetes Dashboard

This repository contains an interactive **Flask + Plotly** [dashboard](https://diabetes-ml-flask-ht3m.onrender.com/) for exploring the **Pima Indians Diabetes dataset** and visualizing the performance of different machine learning classifiers. The dashboard showcases **EDA plots**, **model metrics**, **confusion matrices**, and **feature importances** for Logistic Regression, XGBoost, and a Neural Network. The notebook that contains the EDA and model training is also available in the repo and is very easy to run and experiment with (Bear in mind this is hosted on a free service so it may occasionally present issues with loading).

---

<img width="1661" height="603" alt="image" src="https://github.com/user-attachments/assets/1f12bd2b-a514-4f81-a257-c86e532a9f1b" />

<img width="1681" height="565" alt="image" src="https://github.com/user-attachments/assets/e6e94c2f-5432-43a2-add1-374ae3a65ab8" />


## **Dataset**

The Pima Indians Diabetes dataset contains medical measurements of female patients aged 21 and older.  
- **Features (8 total):** Glucose concentration, BMI, Blood Pressure, Skin Thickness, Insulin, Diabetes Pedigree Function, Age, etc.  
- **Target:** Binary indicator of diabetes (1 = diabetic, 0 = non-diabetic).  

## Features

### Exploratory Data Analysis (EDA)
- Scatter plots and histograms to visualize relationships between features and the target.
- Correlation heatmaps to identify feature dependencies.

### Model Performance
- Metrics comparison: Accuracy, F1 score, AUC-ROC.
- Confusion matrices for Logistic Regression, XGBoost, and Neural Network.
- Feature importance plots to identify key predictors.
