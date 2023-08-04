import json
from flask import Response
from unit_test_python_lib import insert_client
class InsertClient():
    def __init__(self):
        self.client = None
    def execute(self):
        if not self.client:
            return 
        insert_client('/Users/lucascastro/Projects/unit-test-python/unit_test_python/data/clients.json', self.client)
        return '', 201
            

class UpdateClient():
    def __init__(self):
        self.id=None
        self.data=None
    def execute(self):
        with open('../data/clients.json', 'r') as file:
            clients = json.laod(file)
        client = [client for client in clients if client['id'] == id]
class DeleteClient():
    def __init__(self):
        pass
    def execute(self):
        pass
