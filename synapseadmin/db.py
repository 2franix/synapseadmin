#!/usr/bin/python3

import psycopg2

class Database(object):
    def __init__(self, user, passwd):
        passwd = None
        with open(passwd_file, 'r') as f:
            passwd = f.readline()
        self.connection = psycopg2.connect(database='synapse', user='synapse_user', password=passwd)

    def close(self):
        self.connection.close()

    def run_request(self, request):
        cursor = self.connection.cursor()
        cursor.execute(request)
        results = cursor.fetchall()
        cursor.close()
        return results
