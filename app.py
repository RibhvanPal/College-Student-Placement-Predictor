from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open("model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        float_features=[
                float(request.form['IQ']),
                float(request.form['Prev_Sem_Result']),
                float(request.form['CGPA']),
                float(request.form['Academic_Performance']),
                float(request.form['Internship_Experience']),
                float(request.form['Extra_Curricular_Score']),
                float(request.form['Communication_Skills']),
                float(request.form['Projects_Completed'])
        ]
        features= [np.array(float_features)]
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        # Format output
        output = "Placed" if prediction == 1 else "Not Placed"
        return render_template("index.html", prediction_text=f"Placement Status: {output}")
    except (ValueError, KeyError):
        return render_template("index.html", prediction_text="Error: Please enter valid numeric inputs")

if __name__ == "__main__":
    app.run(debug=True)