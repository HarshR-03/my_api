# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from flask import Flask, request, jsonify,render_template, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('reg_model.pkl','rb'))

@app.route('/',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    
    prediction = model.predict(np.array(list(data.values())))
    output = prediction[0]
    return jsonify(output)

if name == "__main__":
    app.run(debug=True)
    
