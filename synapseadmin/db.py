#!/usr/bin/python3

import psycopg2

class Database(object):
    def __init__(self, config):
        self.connection = psycopg2.connect(database='synapse', user=config.database_user, password=config.database_passwd)

    def close(self):
        self.connection.close()

    def run_request(self, request):
        cursor = self.connection.cursor()
        cursor.execute(request)
        results = cursor.fetchall()
        cursor.close()
        return results
