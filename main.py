from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("models/logistic_regression.joblib")
scaler = joblib.load("models/scaler.joblib")


class StudentInput(BaseModel):
    age: int
    gender: str

    cgpa: float
    internships: int
    projects: int

    coding_skills: float
    communication_skills: float
    aptitude_test_score: float

    soft_skills_rating: float
    certifications: int
    backlogs: int

    degree: str
    branch: str


class PredictionResponse(BaseModel):
    prediction: str
    placement_probability: float


def transform_input(student: StudentInput):

    gender = 0 if student.gender == "Male" else 1

    degree_bsc = 1 if student.degree == "B.Sc" else 0
    degree_btech = 1 if student.degree == "B.Tech" else 0
    degree_bca = 1 if student.degree == "BCA" else 0
    degree_mca = 1 if student.degree == "MCA" else 0

    branch_cse = 1 if student.branch == "CSE" else 0
    branch_civil = 1 if student.branch == "Civil" else 0
    branch_ece = 1 if student.branch == "ECE" else 0
    branch_it = 1 if student.branch == "IT" else 0
    branch_me = 1 if student.branch == "ME" else 0

    return [
        [
            student.age,
            gender,
            student.cgpa,
            student.internships,
            student.projects,
            student.coding_skills,
            student.communication_skills,
            student.aptitude_test_score,
            student.soft_skills_rating,
            student.certifications,
            student.backlogs,
            degree_bsc,
            degree_btech,
            degree_bca,
            degree_mca,
            branch_cse,
            branch_civil,
            branch_ece,
            branch_it,
            branch_me,
        ]
    ]


@app.get("/")
def home():
    return {"message": "FastAPI is working!"}


@app.get("/health")
def health():
    return {"status": "Running"}


@app.post("/predict", response_model=PredictionResponse)
def predict(student: StudentInput):

    features = transform_input(student)

    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    probability = model.predict_proba(features_scaled)[0].max()

    prediction_label = "Placed" if prediction == 1 else "Not Placed"

    return {
        "prediction": prediction_label,
        "placement_probability": round(float(probability), 4),
    }
