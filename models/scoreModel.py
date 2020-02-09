from config.configDB import db
import json
from utils.extensions import *

RANK = ('F','D','D+','C','C+','B','B+','A')
class Score(db.Document):

    subject_code = db.StringField(required = True,unique=True)
    subject_name = db.StringField(required = True)
    tc           = db.IntField(required = True)
    tk10         = db.FloatField(max_value=10,min_value=0,required = True)
    tkch         = db.StringField(required = True,choices= RANK)
    tk4          = db.FloatField(max_value=4,min_value=0,required = True)

def createSubjectScore(payload):
    newScore = Score(
        subject_code = payload['subject_code'],
        subject_name = payload['subject_name'],
        tc           = payload['tc'],
        tk10         = payload['tk10'],
        tkch         = exportRank(payload['tk10']),
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
