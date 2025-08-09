from flask import Flask,render_template,request,redirect,url_for
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('CKD.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods=['POST','GET'])
def prediction():
    return render_template('indexnew.html')

@app.route('/predict',methods=['POST'])
def predict():

    input_features=[]    
        
    input_features.append(1.0 if request.form['red_blood_cells'].lower()=='yes' else 0.0)
    input_features.append(1.0 if request.form['pus_cell'].lower()=='yes' else 0.0)
    input_features.append(float(request.form['blood_glucose_random']))
    input_features.append(float(request.form['blood_urea']))
    input_features.append(1.0 if request.form['pedal_edema'].lower()=='yes' else 0.0)
    input_features.append(1.0 if request.form['anemia'].lower()=='yes' else 0.0)
    input_features.append(1.0 if request.form['diabetesmellitus'].lower()=='yes' else 0.0)
    input_features.append(1.0 if request.form['coronary_artery_disease'].lower()=='yes' else 0.0)
    

    features_value=np.array(input_features)

    features_name=['red_blood_cells','pus_cell','blood_glucose_random','blood_urea','pedal_edema','anemia','diabetesmellitus','coronary_artery_disease']

    df=pd.DataFrame([features_value],columns=features_name,index=None)


    output=model.predict(df)[0]

    if output==1:
        prediction_status='negative'
    elif output==0:
        prediction_status='positive'
    else:
        prediction_status='error'        

    return render_template('result.html',prediction_status=prediction_status)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)