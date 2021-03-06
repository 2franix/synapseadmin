#!/usr/bin/python3

import json

class Config(object):
    def __init__(self, config_file):
        config_json = None
        with open(config_file, 'r') as f:
            config_json = json.loads(f.read())
        self._synapse_admin_access_token = config_json['synapse']['accessToken']
        self._db_user = config_json['database']['user']
        self._db_passwd = config_json['database']['password']

    @property
    def synapse_access_token(self):
        return self._synapse_admin_access_token

    @property
    def database_user(self):
        return self._db_user

    @property
    def database_passwd(self):
        return self._db_passwd
