import json
import requests
import os

def GetBearer():

    UID = os.environ['UID']
    SECRET = os.environ['SECRET']

    payload = {'grant_type':'client_credentials', 'client_id':UID, 'client_secret': SECRET}
    try:
        body = requests.post("https://api.intra.42.fr/oauth/token", data=payload)
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps("intra.42.fr endpoint error {}".format(str(e)))}
    tokenInfo = json.loads(body.content)
    bearer = tokenInfo['access_token']
    return bearer

def projects(event, context):


    if 'path' not in event:
        return {"statusCode": 400, "body": json.dumps("Missing id param!")}
    params = event['path']

    if 'id' not in params:
        return {"statusCode": 400, "body": json.dumps("Missing id param!")}
    if str(params['id']) not in ("20133", "40802"):
        return {"statusCode": 400, "body": json.dumps("Sorry but we only allow ryaoi's id :(")}

    bearer = GetBearer()
    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer {}'.format(bearer)})
    try:
        response = session.get('https://api.intra.42.fr/v2/users/{}'.format(params['id']))
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps("intra.42.fr/v2/user/{} endpoints error {}".format(params['id'], str(e)))}

    ryaoiInfo = json.loads(response.content)

    response = {
        "statusCode": 200,
        "Content-Type": "application/json",
        "body": json.dumps(ryaoiInfo['projects_users'])
    }

    return response

