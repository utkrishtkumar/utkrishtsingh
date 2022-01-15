from django.shortcuts import render
from django.http import HttpResponse

import pyrebase

config={
    "apiKey": "AIzaSyCc-QRqVJ967yk2t1Ffl6a3S7Z7rJLDxfA",
    "authDomain": "kivo-6c302.firebaseapp.com",
    "databaseURL": "https://kivo-6c302-default-rtdb.firebaseio.com",
    "projectId": "kivo-6c302",
    "storageBucket": "kivo-6c302.appspot.com",
    "messagingSenderId": "1071748365234",
    "appId": "1:1071748365234:web:f56e3862bca6021e6cc2ab",
    "measurementId": "G-XQCKQQFHEQ"

}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
def home(request):
    
    question1 = database.child('Question1').get().val()
    option1 = database.child('q1s1').get().val()
    option2 = database.child('q1s2').get().val()
    option3 = database.child('q1c1').get().val()
    option4 = database.child('q1c2').get().val()

    

    context = {
        
        "question1" : question1,
        "option1" : option1,
        "option2" : option2,
        "option3" : option3,
        "option4" : option4,
        

    }
        
    hexing = database.child('RRB').get().val()
   # fruit = database.child('Data').child('Name').get().val()
    return render(request, "main/base.html", context)


    
