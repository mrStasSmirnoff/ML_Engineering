from flask import request
import pandas as pd
import numpy as np
import json

data = pd.read_csv('./input/test.csv')
data = data.to_dict('records')
data_json = {'data': data}

headers = {'content-type': "application/json",
           'cache-control': "no-cache",
           }


r = request.get(url='https://mlapi-titanic.herokuapp.com/predictions', headers=headers, data=json.dumps(data_json))
data = r.json()
print(data)