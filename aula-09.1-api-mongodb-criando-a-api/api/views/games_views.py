from flask_restful import Resource
from api import api

class GameList(Resource):
    def get(self):
        return "Olá, mundo! API rodando!"
    
class RecursosAPI(Resource):
    def get(self):
        return "Você enviou uma requisição do tipo GET. O método GET é usado para solicitar informações."
    
    def post(self):
        return "Você enviou uma requisição do tipo POST. O método POST é usado para enviar dados para o servidor e criar novos recursos."
    
    def put(self):
        return "Você enviou uma requisição do tipo PUT. O método PUT é usado para atualizar ou substituir completamente um recurso existente."
    
    def delete(self):
        return "Você enviou uma requisição do tipo DELETE. O método DELETE é usado para excluir um recurso específico do servidor."

api.add_resource(GameList, '/games')
api.add_resource(RecursosAPI, '/recursos')
