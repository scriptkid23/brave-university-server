
# from flask_jwt_extended import decode_token

# def checkPermission(token,Model):

def exportRank(value):
    if value >= 8.5 and value <= 10:
        return 'A'
    if value >=8 and value <= 8.4:
        return 'B+'
    if value >= 7 and value <= 7.9:
        return 'B'
    if value >= 6.5 and value <= 6.9:
        return 'C+'
    if value >= 5.5 and value <= 6.4:
        return 'C'
    if value >= 5.0 and value <= 5.4:
        return 'D+'
    if value >= 4.0 and value <= 4.9:
        return 'D'
    else :
        return 'F'
