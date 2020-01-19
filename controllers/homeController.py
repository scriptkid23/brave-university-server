from flask import Response, request
from models.employeeModel import *
from flask_restful import Resource

class HomeController(Resource):
    def get(self):
        return Response("<h1>Welcome to BRU</h1>",
        mimetype="text/html")

    
    