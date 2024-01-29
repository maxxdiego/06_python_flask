from ..models import game_model
from api import db

def cadastrar_game(game):
    game_bd = game_model.Game(titulo=game.titulo, descricao=game.descricao, data_lancamento=game.data_lancamento)
    db.session.add(game_bd)
    db.session.commit()
    return game_bd

def listar_games():
    games = game_model.Game.query.all()
    return games

def listar_game_id(id):
    game = game_model.Game.query.filter_by(id=id).first()
    return game

def altera_game(game_anterior, game_novo):
    game_anterior.titulo = game_novo.titulo
    game_anterior.descricao = game_novo.descricao
    game_anterior.data_lancamento = game_novo.data_lancamento
    db.session.commit()

def remove_game(game):
    db.session.delete(game)
    db.session.commit()