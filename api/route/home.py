from http import HTTPStatus
from unittest import result
from flask import Blueprint
from flasgger import swag_from
from api.model.WelcomeModel import WelcomeModel
from api.schema.Welcome import WelcomeSchema
from api.model.TosModel import TosModel
from api.schema.Tos import TosSchema

home_api = Blueprint('api', __name__)


@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the NANP API KIT',
            'schema': WelcomeSchema
        },
        HTTPStatus.NOT_FOUND.value:{
            'description':'test of not found'
        }
    }
})
def hello():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = WelcomeModel()
    result.produit(10)
    return WelcomeSchema().dump(result), 200


@home_api.route('/thanks')
def thanks():
    return f'Hello, thanks!'


@home_api.route('/tos')
def tos():
    result=TosModel()
    return TosSchema().dump(result), 200
