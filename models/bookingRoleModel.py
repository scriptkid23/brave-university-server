from config.configDB import db
from datetime import datetime
from utils.createID import encodedID
import json 



# defined  count boooking room number

class BookingRole(db.Document):
    
    booking_role = db.StringField()
    booking_role_limited = db.StringInt()


    