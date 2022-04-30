from dataclasses import fields
from flask_marshmallow import Schema
from marshmallow.fields import Str


class TosSchema(Schema):
    class Meta:
        fields = ['url', 'description']

    message = Str()
