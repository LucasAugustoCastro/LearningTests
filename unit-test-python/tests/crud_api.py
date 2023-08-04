import pytest
from unit_test_python.apis.crud import get_client, Api
from flask import Response

def test_get_return_user(monkeysession):
    def find(*args, **kwargs):
        return {"name": "Rodrigo", "idade": 23, "cpf": "08058096946", "id": "2bc0ec47-df1b-426b-9e18-23ee60bc9fa0"}
    monkeysession.setattr("unit_test_python_lib.Client.find", find)
    client = get_client("2bc0ec47-df1b-426b-9e18-23ee60bc9fa0")
    assert client['id'] == "2bc0ec47-df1b-426b-9e18-23ee60bc9fa0"
    assert client['name'] == 'Rodrigo'

def test_user_not_found(monkeysession):
    def find_client(*args, **kwargs):
        return ''
    monkeysession.setattr("unit_test_python_lib.Client.find", find_client)
    client = get_client("2bc0ec47-df1b-426b-9e18-23ee60bc9fa0")
    response = client.get_json() 
    assert client.status_code == 404
    assert response['message'] == "Client not found"