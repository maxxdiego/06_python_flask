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
            ano = request.json["ano"]
            descricao = request.json["descricao"]
            
            new_game = game_model.Game(titulo=titulo, ano=ano, descricao=descricao)
            result = game_service.add_game(new_game)
            res = g.jsonify(result)
            return make_response(res, 201) #Código 201 (CREATED): Criação bem-sucedida de um novo recurso.
        
class GameDetail(Resource):
    def get(self, id):
        game = game_service.get_game_by_id(id)
        if game is None:
            return make_response(jsonify("Game não foi encontrado"), 404) #Código 404 (NOT FOUND): Indica que o recurso requisitado não foi encontrado no servidor.
        g = game_schema.GameSchema()
        return make_response(g.jsonify(game), 200)
    
    def put(self, id):
        game_bd = game_service.get_game_by_id(id)
        if game_bd is None:
            return make_response(jsonify("Game não foi encontrado"), 404)
        g = game_schema.GameSchema()
        validate = g.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            titulo = request.json["titulo"]
            ano = request.json["ano"]
            descricao = request.json["descricao"]
            new_game = game_model.Game(titulo=titulo, ano=ano, descricao=descricao)
            game_service.update_game(new_game, id)
            updated_game = game_service.get_game_by_id(id)
            return make_response(g.jsonify(updated_game), 200)
        
    def delete(self, id):
        game_bd = game_service.get_game_by_id(id)
        if game_bd is None:
            return make_response(jsonify("Game não encontrado."), 404)
        game_service.delete_game(id)
        return make_response(jsonify("Game excluído com sucesso!"), 204) #Código 204 (NO CONTENT) : Indica que a requisição foi bem sucedida, mas não há conteúdo para retornar ao cliente.
        
api.add_resource(GameList, '/games')
api.add_resource(GameDetail, '/games/<id>')