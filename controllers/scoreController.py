from flask import Response, request
from models.scoreModel import *
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from mongoengine.errors import * 
import json
# Lấy ra tất cả danh sách nhân viên 
class ScoreController(Resource): 
    def get(self):

        payload = getScoreList()
        # print(get_jwt_identity()) // lấy employee_id 
        return Response(payload, mimetype="application/json", status=200)
    def post(self):
        try:
            payload = request.get_json()
            createSubjectScore(payload)
            return Response(json.dumps({'status':200,'message':'create score succeeded'}), mimetype="application/json",status=200)
        except NotUniqueError:
            return Response(json.dumps({'status':400,'message':'subject is exist'}),mimetype="application/json",status=400)
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
