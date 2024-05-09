from api import mongo
from ..models import game_model

def add_game(game):
    mongo.db.games.insert_one({
        'titulo': game.titulo,
        'descricao': game.descricao,
        'ano': game.ano
    })
