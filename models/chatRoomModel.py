from config.configDB import db
import json 


class Message(db.Document):
    content = db.StringField()
    send_by = db.StringField()
    room_by = db.StringField()
