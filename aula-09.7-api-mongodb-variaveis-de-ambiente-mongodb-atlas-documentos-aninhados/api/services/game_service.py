from api import mongo
from ..models import game_model
from bson import ObjectId

def add_game(game):
    mongo.db.games.insert_one({
        'titulo': game.titulo,
        'ano': game.ano,
        'descricao': game.descricao
    })

@staticmethod
def get_games():
    return list(mongo.db.games.find())

@staticmethod
def get_game_by_id(id):
    return mongo.db.games.find_one({'_id': ObjectId(id)})

def update_game(game, id):
    mongo.db.games.update_one({'_id': ObjectId(id)},
    {'$set':
        {
        'titulo': game.titulo,
        'ano': game.ano,
        'descricao': game.descricao
        }
    })

@staticmethod
def delete_game(id):
    mongo.db.games.delete_one({'_id': ObjectId(id)})