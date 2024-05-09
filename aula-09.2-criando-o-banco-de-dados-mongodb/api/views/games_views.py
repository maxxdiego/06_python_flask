from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from ..models import game_model
from ..services import game_service

class GameList(Resource):
    def get(self):
        return "Olá, mundo! API rodando!"    

api.add_resource(GameList, '/games')