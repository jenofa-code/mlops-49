from pathlib import Path

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "student_model.pkl"
MODEL_VERSION = "2.0"

# The Dockerfile trains and creates this model before starting the app.
model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"])
            attendance = float(request.form["attendance"])
            internal_marks = float(request.form["internal_marks"])

            if not (0 <= study_hours <= 24 and 0 <= attendance <= 100
                    and 0 <= internal_marks <= 100):
                raise ValueError("Values are outside the allowed ranges.")

            result = model.predict(
                np.array([[study_hours, attendance, internal_marks]])
            )[0]
            prediction = "PASS ✅" if result == 1 else "FAIL ❌"
        except (ValueError, KeyError):
            error = "Enter valid numeric values: hours 0–24, attendance 0–100, marks 0–100."

    return render_template(
        "index.html", prediction=prediction, version=MODEL_VERSION, error=error
    )


if __name__ == "__main__":
    # Listen on all container interfaces; do not use Flask debug mode in deployment.
    app.run(host="0.0.0.0", port=5000, debug=False)
