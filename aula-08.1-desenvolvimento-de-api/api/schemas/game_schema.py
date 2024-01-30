from api import ma
from ..models import game_model
from marshmallow import fields

class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = game_model.Game
        load_instance = True
        fields = ("id", "titulo", "descricao", "data_lancamento")
    
    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_lancamento = fields.Date(required=True)