#!/usr/bin/python3

import requests
import urllib.parse
import json

def get(path):
    reqHeaders = {'Authorization': 'Bearer <accesstoken>'}
    req = requests.get(f'http://localhost:8008{path}', headers=reqHeaders)
    return req.json()

def post(path, body=None):
    reqHeaders = {'Authorization': 'Bearer <accesstoken>'}
    data = None if body == None else json.dumps(body)
    req = requests.post(f'http://localhost:8008{path}', headers=reqHeaders, data=data)
    return req.json()

print(get('/_synapse/admin/v1'))
# response=post(f'/_synapse/admin/v1/purge_history/{urllib.parse.quote("")}',
        # {'delete_local_events': True, 'purge_up_to_ts': 1551398400000})

# print(f'Response: {responseJson}')
# response = json.loads(responseJson)
# print(f'purge id: {response["purge_id"]}')
