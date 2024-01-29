from flask_restful import Resource
from api import api
from ..schemas import game_schema
from flask import request, make_response, jsonify
from ..entidades import game
from ..services import game_service

class GameList(Resource):
    def get(self):
        games = game_service.listar_games()
        g = game_schema.GameSchema(many=True)
        return make_response(g.jsonify(games), 200)
    
    def post(self):
        g = game_schema.GameSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_lancamento = request.json["data_lancamento"]
            
            novo_game = game.Game(titulo=titulo, descricao=descricao, data_lancamento=data_lancamento)
            resultado = game_service.cadastrar_game(novo_game)
            res = g.jsonify(resultado)
            return make_response(res, 201)

class GameDetail(Resource):
    def get(self, id):
        game = game_service.listar_game_id(id)
        if game is None:
            return make_response(jsonify("Game não foi encontrado"), 404)
        g = game_schema.GameSchema()
        return make_response(g.jsonify(game), 200)
    
    def put(self, id):
        game_bd = game_service.listar_game_id(id)
        if game_bd is None:
            return make_response(jsonify("Game não foi encontrado"), 404)
        g = game_schema.GameSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_lancamento = request.json["data_lancamento"]
            novo_game = game.Game(titulo=titulo, descricao=descricao, data_lancamento=data_lancamento)
            game_service.altera_game(game_bd, novo_game)
            game_alterado = game_service.listar_game_id(id)
            return make_response(g.jsonify(game_alterado), 200)

    def delete(self, id):
        game_bd = game_service.listar_game_id(id)
        if game_bd is None:
            return make_response(jsonify("Game não encontrado."), 404)
        game_service.remove_game(game_bd)
        return make_response("Game excluído com sucesso!", 204)
            
api.add_resource(GameList, '/games')
api.add_resource(GameDetail, '/games/<int:id>')