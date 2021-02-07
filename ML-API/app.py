from flask import Flask, jsonify, request, make_response
import pandas as pd
import numpy as np
import sklearn
import pickle
import json
from config import *
from helper_functions import preprocess

app = Flask(__name__)

# this is a simple test to check whether app is working. It should return a simple string.
@app.route("/", methods=["GET"])
def hello():
    return jsonify("hello from ML API")

# if someone sends a get request to this URL of our flask application along with raw data in the form of JSON, 
# we will preprocess the data the same way we did for creating the model, get predictions and send back the prediction results.
# request.get_json() will basically give us the JSON data that was sent with the get request. We convert that data into a dataframe, 
# use our helper function preprocess() to preprocess the dataframe, use the model_name and column names from the config file to basically 
# load the model with pickle and make predictions on the sliced dataframe. After making the predictions, we will create a response dictionary 
# that contains predictions and prediction label metadata and finally convert that to JSON using jsonify and return the JSON back. 
# Remember that 200 is sent as it was a success.
@app.route("/predictions", methods=["GET"])
def predictions():
    data = request.get_json()
    df = pd.DataFrame(data['data'])
    data_all_x_cols = cols
    try:
        preprocessed_df = preprocess(df)
    except:
        return jsonify("Error occured while preprocessing your data for our model!")

    filename = model_name
    loaded_model = pickle.load(open(filename, 'rb'))

    try:
        predictions = loaded_model.predict(preprocessed_df[data_all_x_cols])
    except:
        return jsonify("Error occured while processing your data into our model!")
    print("done")

    response = {'data': list(predictions), 'prediction_label': {'survived': 1, 'not survived': 0}}
    return make_response(jsonify(response), 200)

if __name__ == '__main__':
    app.run(debug=True)
