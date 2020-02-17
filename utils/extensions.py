
# from flask_jwt_extended import decode_token
import collections
import pandas as pd  


# def checkPermission(token,Model):
def convertList(data):
    return loads(dumps(data))

def exportRank(value):
    if value >= 8.5 and value <= 10:
        return 'A'
    if value >=8 and value <= 8.4:
        return 'B+'
    if value >= 7 and value <= 7.9:
        return 'B'
    if value >= 6.5 and value <= 6.9:
        return 'C+'
    if value >= 5.5 and value <= 6.4:
        return 'C'
    if value >= 5.0 and value <= 5.4:
        return 'D+'
    if value >= 4.0 and value <= 4.9:
        return 'D'
    else :
        return 'F'
def checkNullScore(payload):
    if payload['tc'] == '' or payload['tk10'] == '' or payload['tk4'] == '' or payload['hk'] == '':
        return True
    else:
        return False


class Rank:
    data = []
    timeline = []
    list_rank_default = []

    result = []
    def __init__(self,database,timeline,list_rank_default):
        self.data = database
        self.timeline = timeline
        self.list_rank_default = list_rank_default

    def subfExportRank(self,timeline):
        group_1 = []
        group_2 = []
        for i in self.data:
            if(i['years'] == timeline):
                if(i['hk'] == 1):
                    group_1.append(i['tkch'])
                else:
                    group_2.append(i['tkch'])

        result = []
        for j in [group_1, group_2]:
            counter = collections.Counter(j)
            temp = {}
            for i in self.list_rank_default: 
                try:
                    temp[i] = dict(counter)[i]
                except KeyError:
                    temp[i] = 0
            result.append(temp)
        return result

    def exportRank(self):
        result = []
        # for i in self.timeline:
        #     for j in self.subfExportRank(self.timeline):
        #         result.append(j)
        # print(result)
        for i in self.timeline:
            for j in self.subfExportRank(i):
               result.append(j)
        return result 
    def subfGetValueRank(self,rank):
        return [i[rank] for i in self.exportRank()]
    
    def exportDataRank(self):
        obj = {}
        for i in self.list_rank_default:
            obj[i] = self.subfGetValueRank(i)
        self.result = obj    
        return obj
    def getter(self):
        return self.result



def exportTimeLine(data):
        years = []
        for i in data:
            result = i['years']+"."+str(int(i['hk']))
            years.append(result)
        return list(collections.Counter(years).keys())


def convertExcelFile(file):
    FIELD = ['tk10','subject_name','tc','subject_code','tk4','tkch','years','hk','score_of']
    data = pd.read_excel(file)
    if not (sorted(list(data))== sorted(FIELD)):
        return False
    else:
        tmp = data.to_dict(orient="index")
        result = []
        for i in tmp:
            result.append(tmp[i])
        return result

def ExportMessage(data,obj):
    if(len(data) == 0):
        data.append({
            "own" : obj['own'],
            "avatar" : obj['avatar'],
            "message" : [obj['message']]
        })
        return data
    if(data[len(data) - 1]['own'] == obj['own']):
        data[len(data) - 1]['message'].append(
            obj['message']
        )
        return data
    else:
        data.append({
            "own": obj['own'],
            "avatar": obj['avatar'],
            "message": [obj['message']]
        })
        return data