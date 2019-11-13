import pytest
from unittest.mock import Mock, MagicMock
from synapseadmin import client

@pytest.fixture
def services():
    db_client = Mock()
    db_client.run_request = Mock(return_value=(('room1',),('room2',)))
    service_factory = Mock()
    service_factory.make_db_client = Mock(return_value=db_client)
    yield service_factory

@pytest.fixture
def admin_client(services):
    admin_client = client.AdminClient(None, services)
    yield admin_client

def test_get_room_ids(admin_client):
    room_ids = admin_client.get_room_ids()
    assert room_ids == ['room1', 'room2']
