from api import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_lancamento = db.Column(db.Date, nullable=False)
    
    def __init__(self, titulo, descricao, data_lancamento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_lancamento = data_lancamento