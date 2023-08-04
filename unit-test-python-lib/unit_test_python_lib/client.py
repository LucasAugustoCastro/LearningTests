import json
class Client():
    def _load_file(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    def find(self, id, filepath):
        clients = self._load_file(filepath)
        return [client for client in clients if client['id'] == id][0]