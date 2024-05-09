from api import mongo
from ..models import game_model
from bson import ObjectId

def add_game(game):
    mongo.db.games.insert_one({
        'titulo': game.titulo,
        'descricao': game.descricao,
        'ano': game.ano
    })

@staticmethod
def get_games():
    return list(mongo.db.games.find())

@staticmethod
def get_game_by_id(id):
    return mongo.db.games.find_one({'_id': ObjectId(id)})

def update_game(self, id):
    mongo.db.games.update_one({'_id': ObjectId(id)},
    {'$set':
        {
        'titulo': self.titulo,
        'descricao': self.descricao,
        'ano': self.ano
        }
    })