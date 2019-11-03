import os
import pytest
from synapseadmin import config

@pytest.fixture
def sample_config_file(tmpdir):
    print('sample_config_file')
    config_file = os.path.join(tmpdir,'config')
    with open(config_file, 'w') as f:
        f.write('''{
            "synapse": {
                "accessToken" : "access_token_here!"
            },
            "database": {
                "user": "synapse_user",
                "password": "synapse_password_here!"
            }
        }''')

    print(f'yield {config_file}')
    yield config_file

def test_valid_config(sample_config_file):
    print(f'test_valid_config')
    c = config.Config(sample_config_file) 
    assert c.synapse_access_token == 'access_token_here!' 
    assert c.database_user == 'synapse_user' 
    assert c.database_passwd == 'synapse_password_here!' 
