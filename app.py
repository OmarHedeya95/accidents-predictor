from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import joblib
import pandas as pd
from numpy import ceil

app = Flask(__name__)


@app.route('/', methods=['POST']) #/api/
def makecalc():
    data = request.get_json()

    df = pd.DataFrame({
                "Year": data['year'],
                "Month": data['month']

                },
                index = [0]      
            )

    prediction = np.array2string(ceil(model.predict(df)))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'models/regressor.joblib'
    model = joblib.load(modelfile)
    #app.run(debug=True, host='0.0.0.0')
    app.run(host='0.0.0.0', port=8080)