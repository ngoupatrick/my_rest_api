from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from

home_api = Blueprint('api', __name__)

@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': 'teste'
        }
    }
})
def hello():
    return f'Hello, test!'

@home_api.route('/thanks')
def thanks():
    return f'Hello, thanks!'