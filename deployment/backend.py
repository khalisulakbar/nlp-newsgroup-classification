from flask import Flask, jsonify, request
import pickle
import pandas as pd
from preprocess import preprocess_text

app = Flask(__name__)


columns = ["Content"]

with open("model/sitename_classification.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/predict", methods=['GET', 'POST'])
def body_inference():
    if request.method == 'POST':
        data = request.json
        new_data =[data["Content"]]

        new_data = pd.DataFrame([new_data], columns = columns)
        new_data['Content'] = new_data['Content'].apply(preprocess_text)
        res = model.predict(data)

        response = {'code':200, 'status':'OK',
                    'result':{'prediction': str(res[0])}}
        
        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model Churn Prediction"