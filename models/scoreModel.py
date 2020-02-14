from config.configDB import db
import json
from utils.extensions import *
from models.aggregations import *
from bson.json_util import loads,dumps


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
def getScore():

    score_list = Score.objects._collection.find(
            {},
            {
                "hk" : True,
                "_id":False,
                "subject_name" : True,
                "tc" : True,
                "tk10" : True,
                "tk4" : True,
                "tkch" : True,
                "years" : True

            })
    result = loads(dumps(list(score_list)))
    return json.dumps(result)

def deleteScore(payload):
    subject_code_ =  Score.objects.get(subject_code = payload['subject_code']).delete()
    return subject_code_

def updateScore(payload):
    result = Score.objects.get(subject_code = payload["subject_code"]).update(**payload["data"])

def getScoreList():

    score_list = Score.objects._collection.find(
            {},
            {
                "hk" : True,
                "_id":False,
                "subject_name" : True,
                "tc" : True,
                "tk10" : True,
                "tk4" : True,
                "tkch" : True,
                "years" : True

            })
    result = loads(dumps(list(score_list)))
    return result
def getRankList(payload):
        if(payload['years'] == '' or payload['hk'] == '' or payload['tkch'] == ''):
            return []
        else:
            rank_list = Score.objects._collection.find(
            {"years":payload['years'],"hk":payload['hk'],'tkch':payload['tkch']},
            {
                "_id" : False,
               "hk" : True,
               "subject_name" : True,
               "tkch": True,
               "tk10": True,
               "tk4": True,
               "years" : True,
               "tc" : True
            })
            return json.dumps(loads(dumps(list(rank_list))))


def groupRankListFindOne(payload):
        pipeline = [
            {'$match': {'years': payload['years'], 'hk': payload['hk']}},
            {'$group': {'_id': '$tkch', 'total': {'$sum': 1}}}
        ]
        rank_groups = Score.objects.aggregate(pipeline)
        return json.dumps(loads(dumps(rank_groups)))

def groupRankListFindAll():
        pipeline =  [
    {
        '$group': {
            '_id': '$tkch',
            'total': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            '_id': 1
        }
    }
]
        rank_groups = Score.objects.aggregate(pipeline)
        return json.dumps(loads(dumps(rank_groups)))


def exportRankTimeLine():
    RANK_DEFAULT   = ['A','B+','B','C+','C','D+','D','F']
    TITLE_TIMELINE = exportTimeLine(getScoreList())
    pipeline = [
    {
        '$group': {
            '_id': '$years'
        }
    }, {
        '$sort': {
            'years': -1
        }
    }
]
    TIMELINE = Score.objects.aggregate(pipeline)
    timeline = [i['_id'] for i in list(TIMELINE)]

    # print(timeline)
    rank = Rank(list(getScoreList()),sorted(timeline),RANK_DEFAULT)

    result = {"title":TITLE_TIMELINE,"payload":rank.exportDataRank()}
    return result
