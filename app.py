import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)  #This is the start of the function
#Loading the model and fitted scaler
regmodel = pickle.load(open('regmodel.pkl','rb'))
sc = pickle.load(open('scaling.pkl','rb'))

#first page that my website lands..
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
#This function basically receives i/p in the form of json and then converts it into numpy array
#and scales it and give it to the model for prediction and again jsonfy the output
def predict_api():
    data = request.json['data']
    print(data)  #this is the input received from user
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = sc.transform(np.array(list(data.values())).reshape(1,-1))
    print(new_data)
    output = regmodel.predict(new_data)
    print(output[0])  #output will be a 2-dimensional array
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)


