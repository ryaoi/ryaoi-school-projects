import json
import requests
import os

def projects(event, context):
    UID = os.environ['UID']
    SECRET= os.environ['SECRET']

    payload = {'grant_type':'client_credentials', 'client_id':UID, 'client_secret': SECRET}
    try:
        body = requests.post("https://api.intra.42.fr/oauth/token", data=payload)
    except Exception as e:
        return {"statusCode": 404, "body": json.dumps("intra.42.fr endpoint error {}".format(str(e)))}
    tokenInfo = json.loads(body.content)
    bearer = tokenInfo['access_token']

    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer {}'.format(bearer)})
    try:
        response = session.get('https://api.intra.42.fr/v2/users/20133')
    except Exception as e:
        return {"statusCode": 404, "body": json.dumps("intra.42.fr/v2/users/20133 endpoints error {}".format(str(e)))}

    ryaoiInfo = json.loads(response.content)
    response = {
        "statusCode": 200,
        "Content-Type": "application/json",
        "body": json.dumps(ryaoiInfo['projects_users'])
    }

    return response

