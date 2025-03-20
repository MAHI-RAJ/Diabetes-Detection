from flask import Flask, render_template, request
import ML  # Import ML.py for predictions
import w_ml # Import w_ml.py for predictions

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/men")
def men():
    return render_template("men.html")

@app.route("/women")
def women():
    return render_template("women.html")

@app.route("/predict", methods=["POST"])
def predict():
    print("Form Data Received:", request.form)  # Debugging line

    # Check if form_type exists
    if "form_type" not in request.form:
        return "Invalid Form Submission (form_type missing)", 400  # Specific error message
    
    form_type = request.form.get("form_type")
    print("Form Type Received:", form_type)  # Debugging line

    if form_type == "men":
        try:
            glucose = float(request.form["glucose"])
            bp = float(request.form["bp"])
            skin_thickness = float(request.form["skin_thickness"])
            insulin = float(request.form["insulin"])
            bmi = float(request.form["bmi"])
            dpf = float(request.form["dpf"])
            age = int(request.form["age"])

            input_data = [[glucose, bp, skin_thickness, bmi, dpf, age]]
        except KeyError as e:
            return f"Missing field: {str(e)}", 400

    elif form_type == "women":
        try:
            pregnancies = int(request.form["pregnancies"])
            glucose = float(request.form["glucose"])
            bp = float(request.form["bp"])
            skin_thickness = float(request.form["skin_thickness"])
            insulin = float(request.form["insulin"])
            bmi = float(request.form["bmi"])
            dpf = float(request.form["dpf"])
            age = int(request.form["age"])

            input_data = [[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]]
        except KeyError as e:
            return f"Missing field: {str(e)}", 400

    else:
        return "Invalid Form Submission (Unknown form_type)", 400

    if form_type=="women":
    # Call prediction function from ML.py
      prediction = ML.predict_disease(input_data)

      return render_template("result.html", prediction=prediction)
    else:
        prediction= w_ml.predict_disease(input_data)

        return render_template("result.html", prediction=prediction)


import os
print("Current Working Directory:", os.getcwd())

if __name__ == "__main__":
    app.run(debug=True)
