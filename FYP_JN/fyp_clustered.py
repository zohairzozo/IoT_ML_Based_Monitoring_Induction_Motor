import pandas as pd 
import numpy as np 
import seaborn as sns 
from sklearn.cluster import KMeans 
from scipy.stats import zscore
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt 
import joblib


lr = joblib.load('km.pkl')
print ('Model loaded')
model_columns = joblib.load('km_columns.pkl')
print ('Model columns loaded')

from flask import Flask, request, jsonify,redirect,url_for
import traceback

output = []

app = Flask(__name__)
@app.route('/')
def predict(pred):
    # if lr:
    #     try:
    #         json_ = request.json
    #         query = pd.DataFrame(json_)
    #         print(query)

    #         prediction = list(lr.predict(query))

    #         return jsonify({'prediction': str(prediction)})

    #     except:

    #         return jsonify({'trace': traceback.format_exc()})
    # else:
    
    # if len(output)==0:
    #     return "nothing"
    # else:
    return pred
    
@app.route("/hello", methods=['POST'])
def hello():

    input = request.get_json()
    print(input)
    
    query = pd.io.json.json_normalize(input)
    print(query)
    output.append(list(lr.predict(query))[0])
    
    print("prediction : ",output)
    return "output is " + str(output)
    

app.run(port=1234, debug=True)