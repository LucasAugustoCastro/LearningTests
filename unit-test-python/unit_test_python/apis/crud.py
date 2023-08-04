import json
import logging
from flask import Blueprint, jsonify, request, Response

from unit_test_python import factory
from unit_test_python_lib import Api


api = Blueprint('crud-api', __name__, url_prefix='/crud/client')
LOGGER = logging.getLogger()
@api.route('/<id>', methods=['GET'])
def get_client(id):
    LOGGER.info('Searching client')
    api = Api()
    client = api.client.find(id, '/Users/lucascastro/Projects/unit-test-python/unit_test_python/data/clients.json')
    # client = api.find_client('/Users/lucascastro/Projects/unit-test-python/unit_test_python/data/clients.json', id)
    if not client:
        LOGGER.info('Client not found')        
        
        # return '{"message": "Client not found"}', 404, {"Content-Type": "application/json"}
        return Response(response='{"message": "Client not found"}',status=404, mimetype='application/json')
    return client

@api.route('/', methods=['POST'])
def post_client():
    data = request.get_json()
    if not data.get('cpf'):
        return Response(response='{"message": "Client not found"}',status=404, mimetype='application/json')
    service = factory.insert_client()
    service.client = data
    response = service.execute()
    return response


@api.route('/', methods=['PATCH'])
def update_client(data):
    data = request.get_json()
    if not data.get('id'):
        return Response(status=404).set_data(jsonify({'message': 'Client not found'}))
    service = factory.update_client(data)
    response = service.execute()
    return jsonify(response)

@api.route('/', methods=['DELETE'])
def delete_client(data):
    data = request.get_json()
    if not data.get('id'):
        return Response(status=404).set_data(jsonify({'message': 'Client not found'}))

    service = factory.insert_client(data)
    response = service.execute()
    return jsonify(response)
