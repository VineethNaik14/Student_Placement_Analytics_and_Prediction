# Student Placement Analytics and Prediction

### A machine learning classification project that predicts campus placement outcomes based on academic performance, technical skills, certifications, internships, and project experience.

---
### Dataset

* **Source:** [Kaggle Student Placement Dataset](https://www.kaggle.com/datasets/sonalshinde123/student-placement-dataset)
* **Size:** 45,000 records, 15 features
* **Note:** This is a synthetic dataset generated using predefined logical patterns rather than real-world records.

---
### Exploratory Data Analysis

* **Positive Indicators:** Aptitude test scores, coding skills, and number of projects showed the strongest positive correlation with placement.
* **Negative Indicators:** Number of backlogs significantly reduced placement probability.
* **Negligible Impact:** Age and gender showed no meaningful variance between placed and unplaced students.

---
### Preprocessing

* Dropped `Student_ID` (non-predictive identifier).
* Label Encoding applied to `Gender`.
* One-Hot Encoding applied to `Degree` and `Branch`.
* Applied `StandardScaler` for Logistic Regression.
* Train/Test split: 80/20.

---
### Model Performance

| Model | Accuracy |
| --- | --- |
| Logistic Regression | 86.47% |
| Decision Tree | 100.00% |
| Random Forest | 100.00% |

---
### Technical Note on Accuracy

The tree-based models (Decision Tree, Random Forest) achieved perfect 100% accuracy, which was verified using 5-fold cross-validation.

Feature importance analysis and tree visualization revealed that the models simply extracted the exact mathematical rules used to generate this synthetic dataset (primarily evaluating projects, coding skills, and backlogs). Because real-world placement data contains human variance and unpredictability, the 86.47% accuracy from the Logistic Regression model serves as a more realistic baseline for this type of classification problem.

---
### Tech Stack

* Python, Pandas
* Scikit-learn
* Matplotlib, Seaborn
* Jupyter Notebook

---
Future enhancements include model deployment using Streamlit, evaluation on real-world placement datasets, and comparison with advanced ensemble methods such as Gradient Boosting and XGBoost.
---
## API Deployment (In Progress)

A FastAPI-based inference service has been developed to serve real-time placement predictions.

Current Features:
- FastAPI REST API
- Pydantic request validation
- Logistic Regression model loading via Joblib
- Feature transformation and scaling
- Real-time prediction endpoint

Features to add:
- PostgreSQL prediction logging
- Docker containerization
- Render deployment
- GitHub Actions CI/CD

### Author : `Vineeth Naik`