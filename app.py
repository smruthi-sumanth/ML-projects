from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Gender=request.form.get('gender'),
            Age=float(request.form.get('age')),
            Height=float(request.form.get('height')),
            Weight=float(request.form.get('weight')),
            family_history_with_overweight=request.form.get('family_history_with_overweight'),
            FAVC=request.form.get('FAVC'),
            FCVC=float(request.form.get('FCVC')),
            NCP=float(request.form.get('NCP')),
            CAEC=request.form.get('CAEC'),
            SMOKE=request.form.get('SMOKE'),
            CH2O=float(request.form.get('CH2O')),
            SCC=request.form.get('SCC'),
            FAF=float(request.form.get('FAF')),
            TUE=float(request.form.get('TUE')),
            CALC=request.form.get('CALC'),
            MTRANS=request.form.get('MTRANS')
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
