import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

np.random.seed(42)
n = 500
study_hours = np.random.randint(1, 11, n)
attendance = np.random.randint(50, 101, n)
internal_marks = np.random.randint(20, 51, n)

result = ((study_hours >= 4) & (attendance >= 70) & (internal_marks >= 30)).astype(int)

data = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "internal_marks": internal_marks,
    "result": result
})

X = data[["study_hours", "attendance", "internal_marks"]]
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "student_model.pkl")
print("Model trained and saved as student_model.pkl")
