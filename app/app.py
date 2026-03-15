from flask import Flask, request, render_template_string
import joblib
import os
import numpy as np

app = Flask(__name__)

# Correct model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "model", "student_score_model.pkl")

model = joblib.load(model_path)

html_page = """
<h2>Student Score Predictor</h2>

<form method="post" action="/predict">
Hours Studied:<br>
<input type="number" name="hours_studied"><br>

Attendance:<br>
<input type="number" name="attendance"><br>

Sleep Hours:<br>
<input type="number" name="sleep_hours"><br>

Previous Score:<br>
<input type="number" name="previous_score"><br>

Internet Usage:<br>
<input type="number" name="internet_usage"><br><br>

<input type="submit" value="Predict Score">
</form>

{% if prediction %}
<h3>Predicted Score: {{prediction}}</h3>
{% endif %}
"""

@app.route("/")
def home():
    return render_template_string(html_page)

@app.route("/predict", methods=["POST"])
def predict():

    hours = float(request.form["hours_studied"])
    attendance = float(request.form["attendance"])
    sleep = float(request.form["sleep_hours"])
    previous = float(request.form["previous_score"])
    internet = float(request.form["internet_usage"])

    features = np.array([[hours, attendance, sleep, previous, internet]])

    prediction = model.predict(features)[0]

    return render_template_string(html_page, prediction=round(prediction, 2))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))