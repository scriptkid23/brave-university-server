from config.configDB import db
import json 
from mongoengine.errors import *
class Score(db.Document):
    
    subject_code = db.StringField(required = True,unique=True)
    subject_name = db.StringField(required = True)
    tc           = db.StringField(required = True)
    tk10         = db.StringField(required = True)
    tkch         = db.StringField(required = True)
    tk4          = db.StringField(required = True)

def createSubjectScore(payload):
    newScore = Score(
        subject_code = payload['subject_code'],
        subject_name = payload['subject_name'],
        tc           = payload['tc'],
        tk10         = payload['tk10'],
        tkch         = payload['tkch'],
        tk4          = payload['tk4'],
    )
    newScore.save()
def getScoreList():
    data = Score.objects().to_json()
    return data

def deleteScore(payload):
    subject_code_ =  Score.objects.get(subject_code = payload['subject_code']).delete()
    return subject_code_

def updateScore(payload): 
    result = Score.objects.get(subject_code = payload["subject_code"]).update(**payload["data"])
    