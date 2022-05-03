from dataclasses import fields
from email import message
from flask_marshmallow import Schema
from marshmallow import fields
from marshmallow.fields import Str


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
