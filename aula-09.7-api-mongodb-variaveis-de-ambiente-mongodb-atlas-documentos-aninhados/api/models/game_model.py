from api import mongo

class Game():
    def __init__(self, titulo, ano, descricao):
        self.titulo = titulo
        self.ano = ano
        self.descricao = descricao