from config.configDB import db
import json
from utils.extensions import *
from models.aggregations import *
from bson.json_util import loads,dumps
from flask_jwt_extended import get_jwt_claims

RANK = ('F','D','D+','C','C+','B','B+','A')
class Score(db.Document):

    subject_code = db.IntField(required = True,min_length = 1,unique = True)
    subject_name = db.StringField(required = True,min_length = 1)
    tc           = db.IntField(required = True,min_value = 0)
    tk10         = db.FloatField(max_value=10,min_value=0,required = True)
    tkch         = db.StringField(required = True,choices= RANK)
    tk4          = db.FloatField(max_value=4,min_value=0,required = True)
    hk           = db.IntField(required = True,choices = (1,2))
    years        = db.StringField(required = True, min_length = 1)
    score_of     = db.StringField(required = True)
def createSubjectScore(payload):
    if not checkNullScore(payload):
        newScore = Score(
            subject_code = int(payload['subject_code']),
            subject_name = payload['subject_name'],
            tc           = int(payload['tc']),
            tk10         = float(payload['tk10']),
            tkch         = exportRank(float(payload['tk10'])),
            tk4          = float(payload['tk4']),
            hk           = int(payload['hk']),
            years        = payload['years'],
            score_of     = payload['score_of']
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

def getScoreList(score_of):

    score_list = Score.objects._collection.find(
            {"score_of":score_of},
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

def groupRankListFindAll(score_of):
        pipeline =  [
            {
            '$match': {
                'score_of': score_of
            }
            },
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


def exportRankTimeLine(score_of):
    RANK_DEFAULT   = ['A','B+','B','C+','C','D+','D','F']
    print(type(score_of))
    TITLE_TIMELINE = exportTimeLine(getScoreList(score_of))
    pipeline = [
        {
            '$match': {
                'score_of': score_of
            }
        },
    {
        '$group': {
            '_id': '$years'
        }
    }, {
        '$sort': {
            'years': -1
        }
    },
]
    TIMELINE = Score.objects.aggregate(pipeline)
    timeline = [i['_id'] for i in list(TIMELINE)]

    # print(timeline)
    rank = Rank(list(getScoreList(score_of)),sorted(timeline),RANK_DEFAULT)

    result = {"title":TITLE_TIMELINE,"payload":rank.exportDataRank()}
    return result

def uploadScoreFile(file):

    data = convertExcelFile(file)
    print(data)
    result = []
    for i in data:
        result.append(Score(**i))
    Score.objects.insert(result)
    return True
