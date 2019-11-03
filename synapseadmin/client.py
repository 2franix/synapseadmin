#!/usr/bin/python3

import requests
import urllib.parse
import json

class AdminClient(object):
    def __init__(self, config, services):
        self.config = config
        self._db = services.make_db_client()

    def get_room_ids(self):
        """Gets identifiers of all rooms."""
        return [item[0] for item in self._db.run_request('SELECT room_id FROM rooms')]

    def _makeHeaders(self):
        reqHeaders = {'Authorization': f'Bearer {self.config.synapse_access_token}'}
        return reqHeaders

    def _get(path):
        reqHeaders = {'Authorization': 'Bearer <accesstoken>'}
        req = requests.get(f'http://localhost:8008{path}', headers=reqHeaders)
        return req.json()

    def _post(path, body=None):
        reqHeaders = {'Authorization': 'Bearer <accesstoken>'}
        data = None if body == None else json.dumps(body)
        req = requests.post(f'http://localhost:8008{path}', headers=reqHeaders, data=data)
        return req.json()

#print(get('/_synapse/admin/v1'))
# response=post(f'/_synapse/admin/v1/purge_history/{urllib.parse.quote("")}',
        # {'delete_local_events': True, 'purge_up_to_ts': 1551398400000})

# print(f'Response: {responseJson}')
# response = json.loads(responseJson)
# print(f'purge id: {response["purge_id"]}')
