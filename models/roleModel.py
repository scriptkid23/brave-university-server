from config.configDB import db
import json 

class Role(db.Document):
    
    name        = db.StringField(max_length=255,min_length=1,required=True,unique=True)
    description = db.StringField(max_length=255,default="")
    content     = db.ListField(db.StringField(max_length=255,min_length=1,required=True))

def getListRole():
    result = Role.objects().to_json()
    print((result))