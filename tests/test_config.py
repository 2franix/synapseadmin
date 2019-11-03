import pytest
from synapseadmin import config

@pytest.fixture
def sample_config_file(tmp_path):
    with open(tmp_path, 'w') as f:
        f.write("""{
            'synapse': {
                'accessToken' : 'access_token_here!'
            },
            'database': {
                'user': 'synapse_user',
                'password': 'synapse_password_here!'
            }
        }""")
    yield tmp_path

def test_valid_config(sample_config_file):
   c = config.Config(sample_config_file) 
   assert c.synapse_access_token == 'access_token_here!' 
   assert c.database_user == 'synapse_user' 
   assert c.database_passwd == 'synapse_password_here!' 
