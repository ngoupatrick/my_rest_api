from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from
from api.model.WelcomeModel import WelcomeModel
from api.model.TosModel import TosModel
from api.model.DataModel import DataModel
from api.model.ErrorModel import ErrorModel
from api.model.BDModel import FOR_UPDATE, Personne, User
from api.schema.Welcome import DataSchema, UserSchema, UsersSchema, WelcomeSchema, TosSchema, ErrorSchema, PersonneSchema, PersonnesSchema

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
}, methods=['POST'])
def hello():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    quotient = 2
    if request.method == 'POST':
        quotient = int(request.json.get('quotient', 2))
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


@home_api.route('/personnes')
def personne_list():
    all_personne = Personne.query.all()
    return PersonnesSchema.dumps(all_personne), 200


@home_api.route('/personne', methods=['POST'])
def personne():
    id = int(request.json.get('id', 0))
    la_personne = Personne.query.get(id)
    return PersonneSchema().dump(la_personne), 200


@home_api.route('/new_personne', methods=['POST'])
def new_personne():
    nom = str(request.json.get('nom', ''))
    ville = str(request.json.get('ville'))
    result = 1
    if request.method == 'POST':
        p = Personne(nom=nom, ville=ville)
        result = p.personne()
    if request.method == 'PUT':
        id_p = int(request.json.get('id_personne', 0))
        p = Personne.query.get(id_p)
        p.nom = nom
        p.ville = ville
        result = p.personne(options=FOR_UPDATE)
    if result == 0:
        return PersonneSchema().dump(p), 200
    if result == 1:
        return {"Message": "No Valid parameter"}, 404


@home_api.route('/users')
def user_list():
    all_user = User.query.all()
    return UsersSchema.dumps(all_user), 200


@home_api.route('/user', methods=['POST'])
def user():
    id = int(request.json.get('id', 0))
    login = str(request.json.get('login', ""))
    psw = str(request.json.get('psw', ""))
    le_user = None
    if id != 0:
        le_user = User.query.get(id)
    if login.strip() != "":
        le_user = User.query.filter(User.login == login).one()
        if le_user:
            if le_user.pass_hash == psw:
                return UserSchema().dump(le_user), 200
    return UserSchema().dump(le_user), 200


@home_api.route('/new_user', methods=['POST', 'PUT'])
def new_user():
    login = str(request.json.get('login', ''))
    pw = str(request.json.get('pass'))
    id_p = int(request.json.get('id_personne', 0))
    result = 1
    if request.method == 'POST':
        u = User(login=login, pass_hash=pw, id_personne=id_p)
        result = u.user()
    if request.method == 'PUT':
        id_u = int(request.json.get('id_user', 0))
        u = User.query.get(id_u)
        u.login = login
        u.pass_hash = pw
        u.id_personne = id_p
        result = u.user(options=FOR_UPDATE)
    if result == 0:
        return UserSchema().dump(u), 200
    if result == 1:
        return {"Message": "No Valid parameter"}, 404
