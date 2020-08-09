import pytest
import yaml
from client import *
VAR = {}

@pytest.fixture()
def set():
    def __set(key, value):
        VAR[key] = value
    return __set

@pytest.fixture()
def get():
    def __get(key):
        return VAR.get(key)
    return __get

@pytest.fixture()
def api():
    def __api(name):
        with open(file='./data/template.yaml', mode='r', encoding='utf-8') as f:
            for d in yaml.load(f, yaml.FullLoader)['templates']:
                if d['api'] == name:
                    client = Client(url=d['url'], method=d['method'], body_type=d['body_type'])
                    return client
            else:
                return None
    return __api

