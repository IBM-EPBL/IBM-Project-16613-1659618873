import os
import numpy as np
from flask import Flask, render_template, url_for, request



app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/about')
def home():
    return render_template('about.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=False) 