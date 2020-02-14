from flask import Response, request
from models.scoreModel import *
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from mongoengine.errors import *
import json

ALLOWED_EXTENSIONS = set(['xlsx','xls'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class ScoreController(Resource):
    def get(self):

        result = getScoreList()
        # print(get_jwt_identity()) // lấy employee_id
        return Response(json.dumps(result), mimetype="application/json", status=200)
    def post(self):
        try:
            payload = request.get_json()
            print(payload)

            if createSubjectScore(payload):
                return Response(json.dumps({'status':200,'message':'create score succeeded'}), mimetype="application/json",status=200)
            else:
                return Response(json.dumps({'status':400,'message':'Validation Error'}), mimetype="application/json",status=400)
        except NotUniqueError:
            return Response(json.dumps({'status':400,'message':'subject is exist'}),mimetype="application/json",status=400)
        except ValidationError:
            return Response(json.dumps({'status':400,'message':'Validation Error'}),mimetype="application/json",status=400)
    def delete(self):
        try:
            payload = request.get_json()
            subject_code_ = deleteScore(payload)
            return Response(json.dumps({'status':200,'message':'delete score succeeded'}), mimetype="application/json",status=200)
        except DoesNotExist:
            return Response(json.dumps({'status':400,'message':'delete score failed, Score Does Not Exist'}), mimetype="application/json",status=400)
    def put(self):
        try:
            payload = request.get_json()
            result = updateScore(payload)
            return Response(json.dumps({'status' : 200,'message' : 'update score succeeded'}), mimetype="application/json", status=200)
        except DoesNotExist:
            return Response(json.dumps({'status':400,'message':'update score failed, Score Does Not Exist'}), mimetype="application/json",status=400)



class GetListRankController(Resource):
    def get(self):
        result = groupRankListFindAll()
        return Response(result, mimetype="application/json", status=200)
class GetListRankTimeLineController(Resource):
    def get(self):
        payload = exportRankTimeLine()
        return Response(json.dumps(payload),mimetype="application/json", status=200)

class UploadScoreController(Resource):
    def post(self):
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                result = uploadScoreFile(file)
                return Response(json.dumps({"code" : 200,"status" :"upload succeeded"}),mimetype="application/json", status=200)
            else:
                return Response(json.dumps({"code" : 200,"status" :"upload failed"}), mimetype="application/json", status=400)
        except BulkWriteError:

            return Response(json.dumps({"code" : 200,"status" :"upload failed"}), mimetype="application/json", status=400)
