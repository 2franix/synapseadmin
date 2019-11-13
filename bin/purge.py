#!/usr/bin/python3

import os
from synapseadmin import db, client, config, services

conf = config.Config(os.path.join(__file__, '..', 'creds.json'))
services_factory = services.ConcreteServiceFactory(conf)
admin_client = client.AdminClient(conf, services_factory)

print(admin_client.get_room_ids())
