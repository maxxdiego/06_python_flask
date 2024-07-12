from api import ma
from marshmallow import Schema, fields

class GameSchema(ma.Schema):
    class Meta:
        fields = ("_id", "titulo", "ano", "descricao")

    _id = fields.Str()
    titulo = fields.Str(required=True)
    ano = fields.Int(required=True)
    descricao = fields.Dict(required=True)