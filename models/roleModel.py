from config.configDB import db
import json 

class Role(db.Document):
    
    permission_booking = db.BooleanField(required = True)
    permission_permit_booking = db.BooleanField(required = True)
    permission_delete_list_booking = db.BooleanField(required = True)
    permission_delete_member = db.BooleanField(required = True)
    permission_create_alert = db.BooleanField(required = True)
    permission_default      = db.BooleanField(required = True)

def createRole(payload):
    newRole = Role(
        permission_booking = payload['permission_booking'],
        permission_permit_booking = payload['permission_permit_booking'],
        permission_delete_list_booking = payload['permission_delete_list_booking'],
        permission_delete_member = payload['permission_delete_member'],
        permission_create_alert = payload['permission_create_alert'],
        permission_default      = payload['permission_default']
    )
    newRole.save()
def getRoleDefault():
    roleDefault = Role.objects.get(permission_default = True)
    return roleDefault['id']
