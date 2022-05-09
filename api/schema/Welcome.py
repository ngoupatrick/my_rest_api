from flask_marshmallow import Schema
from marshmallow import fields
from marshmallow.fields import Str

from api.db.db_extensions import ma_obj
from api.model.BDModel import Personne, User


class WelcomeSchema(Schema):
    # Fields to expose
    message = fields.Str()
    state = fields.Bool()
    number = fields.Int()
    resultat = fields.Float()


class TosSchema(Schema):
    url = fields.Str()
    description = fields.Str()


class DataSchema(Schema):
    IP = fields.Str()
    user_agent = fields.Str()


class ErrorSchema(Schema):
    code = fields.Int()
    description = fields.Str()
    # --OLD STYLE
    # class Meta:
    #fields = ['code', 'description']
    #message = Str()


class PersonneSchema(ma_obj.SQLAlchemyAutoSchema):
    class Meta:
        model = Personne


class UserSchema(ma_obj.SQLAlchemyAutoSchema):
    class Meta:
        model = User

PersonnesSchema = PersonneSchema(many=True)
UsersSchema = UserSchema(many=True)
