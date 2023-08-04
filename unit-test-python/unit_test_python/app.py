import logging

from flask import Flask
from flask_cors import CORS
from flask_log_request_id import current_request_id, RequestID

from unit_test_python.apis import crud

LOGGER = logging.getLogger(__name__)

# Desabilita o log das requisições HTTP
logging.getLogger('werkzeug').setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app)
LOGGER.info('Configurado Ext Flask CORS')

RequestID(app)
LOGGER.info('Configurado FlaskRequestId')


app.register_blueprint(crud.api)

LOGGER.info('Registrados blueprints')
