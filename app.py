# Import libraries

import numpy as np
from flask import Flask, request, jsonify
import pickle
from xgboost import XGBRegressor
import pandas as pd
from flask_cors import CORS

# load model
model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

# cors
CORS(app)

# routes
@app.route('/api', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': float(result)}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run()
