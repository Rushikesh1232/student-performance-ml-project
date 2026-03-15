# Student Performance Prediction ML Project

This project predicts a student's final exam score based on study and lifestyle factors using a Machine Learning model.

The model is trained using Python and deployed as a web application using Flask.

--------------------------------------------------

PROJECT WORKFLOW

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Saving
8. Flask API Development
9. Deployment

--------------------------------------------------

TECHNOLOGIES USED

Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  
Scikit-learn  
Flask  
Joblib

--------------------------------------------------

PROJECT STRUCTURE

student-performance-ml-project

data/
    student_data.csv

notebooks/
    EDA.ipynb

model/
    student_score_model.pkl

app/
    app.py

requirements.txt
README.md

--------------------------------------------------

DATASET FEATURES

hours_studied      : number of study hours per day  
attendance         : attendance percentage  
sleep_hours        : sleep hours per day  
previous_score     : previous exam score  
internet_usage     : hours spent on internet  

Target variable:

final_exam_score

--------------------------------------------------

MODEL USED

Linear Regression

--------------------------------------------------

HOW TO RUN THE PROJECT

Step 1 — Clone the repository

git clone https://github.com/YOUR_USERNAME/student-performance-ml-project.git

Step 2 — Navigate to the project folder

cd student-performance-ml-project

Step 3 — Create virtual environment

python -m venv venv

Step 4 — Activate environment

Windows:

venv\Scripts\activate

Step 5 — Install dependencies

pip install -r requirements.txt

Step 6 — Run the Flask application

cd app

python app.py

Step 7 — Open browser

http://127.0.0.1:5000/

Enter input values and get predicted student score.

--------------------------------------------------

SAMPLE INPUT

hours_studied : 6  
attendance : 90  
sleep_hours : 7  
previous_score : 80  
internet_usage : 2  

OUTPUT

Predicted Score: 84.5


AUTHOR

Machine Learning Project
