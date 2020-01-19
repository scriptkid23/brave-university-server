import base64
from datetime import datetime

def encodedID(payload):
    year = str(datetime.utcnow().year)
    month = str(datetime.utcnow().month)
    day = str(datetime.utcnow().day)
    hour = str(datetime.utcnow().hour)
    minute = str(datetime.utcnow().minute)
    second = str(datetime.utcnow().second)
    microsecond = str(datetime.utcnow().microsecond)
    result = year + '-' + month + '-' + day + '-' + hour + '-' + minute + '-' + second + '-' + microsecond + '-' + payload
    encoded = result.encode('ascii')
    return base64.b64encode(encoded).decode('utf-8')

