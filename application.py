from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load model and dataset
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
car = pd.read_csv("Cleaned_Car_data.csv")


@app.route('/')
def index():

    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].dropna().unique())

    companies.insert(0, "Select Company")

    return render_template(
        "index.html",
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types
    )


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():

    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    input_df = pd.DataFrame({
        'name': [car_model],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    prediction = model.predict(input_df)

    return str(round(prediction[0], 2))


if __name__ == "__main__":
    app.run(debug=True)