from config.configDB import db
import json
from utils.extensions import *

RANK = ('F','D','D+','C','C+','B','B+','A')
class Score(db.Document):

    subject_code = db.StringField(required = True,unique=True, min_length = 1)
    subject_name = db.StringField(required = True,min_length = 1)
    tc           = db.IntField(required = True,min_value = 0)
    tk10         = db.FloatField(max_value=10,min_value=0,required = True)
    tkch         = db.StringField(required = True,choices= RANK)
    tk4          = db.FloatField(max_value=4,min_value=0,required = True)
    hk           = db.IntField(required = True,choices = (1,2))
    years        = db.StringField(required = True, min_length = 1)

def createSubjectScore(payload):
    if not checkNullScore(payload):
        newScore = Score(
            subject_code = payload['subject_code'],
            subject_name = payload['subject_name'],
            tc           = int(payload['tc']),
            tk10         = float(payload['tk10']),
            tkch         = exportRank(float(payload['tk10'])),
            tk4          = float(payload['tk4']),
            hk           = int(payload['hk']),
            years        = payload['years']

        )
        newScore.save()
        return True
    else:
        return False
def getScoreList():
    data = Score.objects().to_json()
    return data

def deleteScore(payload):
    subject_code_ =  Score.objects.get(subject_code = payload['subject_code']).delete()
    return subject_code_

def updateScore(payload):
    result = Score.objects.get(subject_code = payload["subject_code"]).update(**payload["data"])
