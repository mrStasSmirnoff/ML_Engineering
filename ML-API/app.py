import Flask, jsonify, request, make_response
import pandas as pd
import numpy as np
import sklearn
import pickle
import json
from config import *
from helper_functions import preprocess

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello():
    return jsonify("hello from ML API")


if __name__ == '__main__':
    app.run(debug=True)