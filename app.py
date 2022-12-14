import pickle
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
app = Flask(__name__, template_folder='templates', static_folder='static')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')   
@app.route('/service')
def service():
    context=['I am currently employed at least part-time', 'Education',
       'I have my own computer separate from a smart phone',
       'I have been hospitalized before for my mental illness',
       'How many days were you hospitalized for your mental illness',
       'I am legally disabled', 'I have my regular access to the internet',
       'I live with my parents', 'I have a gap in my resume',
       'Total length of any gaps in my resume in months.', 'Income',
       'Unemployed', 'I read outside of work and school',
       'Annual income from social welfare programs', 'I receive food stamps',
       'I am on section 8 housing',
       'How many times were you hospitalized for your mental illness',
       'Lack of concentration', 'Anxiety', 'Depression', 'Obsessive thinking',
       'Mood swings', 'Panic attacks', 'Compulsive behavior', 'Tiredness',
       'Age', 'Gender']
    return render_template('home.html',context=context)
    
def ValuePredictor(to_predict_list):
    to_predict = (to_predict_list)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods = ['POST'])

def result():
    if request.method =='POST':
        
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        to_predict_list = list(map(int, to_predict_list))
        print(to_predict_list)

        result = ValuePredictor([to_predict_list])       
        if int(result)== 1:
            prediction ='Prediction show your  metaly Ill'
        else:
            prediction ='Prediction show your are fine'           
        return render_template("result.html", prediction = prediction)
    else:
        return render_template("home.html")
        
if __name__ == '__main__':
    app.run(debug=True)
