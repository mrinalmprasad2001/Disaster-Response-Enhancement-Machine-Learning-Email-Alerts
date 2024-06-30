from flask import Flask, render_template, request , jsonify
import pickle
import numpy as np
import warnings
from alert import mail


# Disable warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

with open('drought_model.pkl', 'rb') as file:
    models = pickle.load(file)

# Load the trained model
with open('flood_rfmodel.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the month names
month_names = [
    'January', 'February', 'March', 'April', 
    'May', 'June', 'July', 'August', 
    'September', 'October', 'November', 'December'
]

@app.route('/')
def index():
    return render_template('index.html', month_names=month_names)

@app.route('/drought')
def drought():
    return render_template('dpredict.html')

@app.route('/fpredict', methods=['POST'])
def fpredict():

    values = [float(request.form[f'month_{i}']) for i in range(1, 13)]
    prediction = model.predict([values])[0]
    if(prediction==1):
        vel="Flood may occur"
 
        mail(f'Hello,\n\nOur machine learning model has predicted a flood chancewith an accuracy of 84%.\nPlease take necessary steps and precautions.')
    else:
        vel="no chance for flood"

    return render_template('result.html', prediction=vel)

@app.route('/dpredict', methods=['POST'])
def dpredict():

    input_values = [float(request.form[f'value{i+1}']) for i in range(9)]
    predictions = models.predict([input_values])[0]
    if(predictions==1):
        vel="drought may occur"
        mail(f'Hello,\n\nOur machine learning model has predicted a drought chance with an accuracy of 89%. \nPlease take necessary steps and precautions.')
    else:
        vel="no chance for drought"

    return render_template('result.html', prediction=vel)

if __name__ == '__main__':
    app.run(debug=True)
