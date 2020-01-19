from config.configDB import db
from datetime import datetime

import json 

class Employee(db.Document):
    employee_id = db.IntField(required=True, unique=True)
    employee_name = db.StringField(max_length=255, required=True)
    employee_gender = db.BooleanField(required=True)
    employee_birthday = db.DateTimeField(required=True)
    employee_avatar = db.StringField()
    def json(self):
        employee_dict = {
            "employee_id": self.employee_id,
            "employee_name": self.employee_name,
            "employee_gender": self.employee_gender,
            "employee_birthday": self.employee_birthday,
            "employee_avatar": self.employee_avatar,

        }
        return json.dumps(employee_dict)
    def get_id(self):
        return unicode(self.employee_id)
    
def createEmloyee(payload):
    newEmployee = Employee(
        employee_id=Employee.objects.count() + 1,
        employee_name=payload["employee_name"],
        employee_gender=payload["employee_gender"],
        employee_birthday=payload["employee_birthday"],
        employee_avatar=payload["employee_avatar"],
    )
    newEmployee.save()

def getEmployees():
    return Employee.objects().to_json()

# def updateEmployee(self,payload):
#     pass #
# def deleteEmployee(self,payload):
