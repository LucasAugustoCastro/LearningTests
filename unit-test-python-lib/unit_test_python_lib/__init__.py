import json
import uuid
from unit_test_python_lib.client import Client

class Api():
    def __init__(self):
        self.client = Client()

    def find_client(self,filepath, id):
       self.client.find(id, filepath)

    def insert_client(filepath, client):
        id = str(uuid.uuid4())
        with open(filepath, 'r') as file:
            clients = json.load(file)
        if not clients:
            clients = []
        client['id']=id
        clients.append(client)
        with open(filepath, 'w') as file:
            json.dump(clients, file)