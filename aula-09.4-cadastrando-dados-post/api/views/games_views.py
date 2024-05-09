from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import game_schema
from ..models import game_model
from ..services import game_service

class GameList(Resource):
    def get(self):
        games = game_service.get_games()
        g = game_schema.GameSchema(many=True)
        return make_response(g.jsonify(games), 200)  #Código 200 (OK): Sucesso na solicitação.
    
    def post(self):
        g = game_schema.GameSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400) #Código 400 (BAD REQUEST): Solicitação inválida ou malformada.
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            ano = request.json["ano"]
            
            new_game = game_model.Game(titulo=titulo, descricao=descricao, ano=ano)
            result = game_service.add_game(new_game)
            res = g.jsonify(result)
            return make_response(res, 201) #Código 201 (CREATED): Criação bem-sucedida de um novo recurso.

api.add_resource(GameList, '/games')