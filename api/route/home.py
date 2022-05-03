from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from
from api.model.WelcomeModel import WelcomeModel
from api.model.TosModel import TosModel
from api.model.DataModel import DataModel
from api.model.ErrorModel import ErrorModel
from api.schema.Welcome import DataSchema, WelcomeSchema, TosSchema, ErrorSchema


home_api = Blueprint('api', __name__)


@home_api.route('/', methods=['GET', 'POST'])
@swag_from({
    "parameters": [
        {
            "name": "quotient",
            "in": "path",
            "type": "integer",
            "required": "true",
            "default": "2"
        }
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the NANP API KIT',
            'schema': WelcomeSchema
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'test of not found'
        }
    }
})  # , methods=['POST']
def hello():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    quotient = 2
    if request.method == 'POST':
        quotient = int(request.json['quotient'])
    result = WelcomeModel()
    result.produit(quotient=quotient)
    return WelcomeSchema().dump(result), 200


@home_api.route('/thanks')
def thanks():
    return f'Hello, thanks!'


@home_api.route('/tos')
def tos():
    result = TosModel()
    return TosSchema().dump(result), 200


@home_api.get(rule='/getMyData')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get your data details',
            'schema': DataSchema
        }
    }
})
def getIP():
    result = DataModel(request=request)
    return DataSchema().dump(result), 200


@home_api.app_errorhandler(404)
def gestionError(error):
    result = ErrorModel(error=error)
    return ErrorSchema().dump(result), 404
