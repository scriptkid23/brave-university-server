from flask import Response, request
from models.employeeModel import *
from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required,get_jwt_identity

import json
import os

ALLOWED_EXTENSIONS = set(['png','jpg','jgeg','gif','pdf'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadImageController(Resource):
    
    def post(self):
       file = request.files['file']
       if file and allowed_file(file.filename):
              upload = os.path.join('./upload/image',file.filename)
              file.save(upload)
              return Response(json.dumps({"message": "upload image success","status":"200"}), mimetype="application/json", status=200)
       else:
              return Response(json.dumps({"message": "upload image failed","status":"400"}), mimetype="application/json", status=400)
