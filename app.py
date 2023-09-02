"""
created on Fri Nov 14 2023
@author: Omkar Nallagoni
"""
"""import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

app= Flask(__name__)

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')       #decorator
def welcome():
    return "welcome all"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    input_cols= ['MedInc','HouseAge',]
    input_cols=["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude" , "Longitude" ] 
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))

    #prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    prediction=classifier.predict([list1])
    print(prediction)
    return"Hello the answer is"+str(prediction)

#list1.append (val)
if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8000)
"""

"""
Created on Fri Nov 14 2019

@author: Omkar Nallagoni
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

#model.pkl is used to get the predictions on new data
# in this page np pd pickle we did not used it is masked
# yellow error 


app=Flask(__name__)

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')      # decorator
def welcome():
    return "Welcome All"


@app.route('/predict',methods=["Get"])
def predict_note_authentication():

    """
     ['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude'
   """
    input_cols= ['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))

    '''
    MedInc=request.args.get("MedInc")
    HouseAge=request.args.get("HouseAge")
    AveRooms=request.args.get("AveRooms")
    AveBedrms=request.args.get("AveBedrms")
    Population=request.args.get("Population")
    AveOccup=request.args.get("AveOccup")
    Latitude=request.args.get("Latitude")
    Longitude=request.args.get("Longitude")'''
    prediction=classifier.predict([list1])

    #prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file', methods=["POST"]) 
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file")) 
    prediction=classifier.predict(df_test)
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)