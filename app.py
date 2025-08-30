from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# مدل لود شده
model = joblib.load("filename.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # گرفتن ورودی‌ها
            features = [
                float(request.form.get("amt")),
                float(request.form.get("lat")),
                float(request.form.get("long")),
                float(request.form.get("city_pop")),
                float(request.form.get("unix_time")),
                float(request.form.get("merch_lat")),
                float(request.form.get("merch_long"))
            ]
            features = np.array(features).reshape(1, -1)

            # پیش‌بینی
            pred = model.predict(features)[0]
            prediction = "Fraud Detected 🚨" if pred == 1 else "Legit Transaction ✅"
        except:
            prediction = "⚠️ Invalid Input! Please enter valid numbers."

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
