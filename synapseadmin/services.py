#!/usr/bin/python3

class ServiceFactory(object):
    def make_db_client(self):
        raise NotImplementedError('Not implemented.')

class ConcreteServiceFactory(ServiceFactory):
    def __init__(self, config):
        self._config = config

    def make_db_client(self):
        return db.Database(self._config)
