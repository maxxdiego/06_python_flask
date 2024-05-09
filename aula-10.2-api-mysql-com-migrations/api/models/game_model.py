from api import db

class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_lancamento = db.Column(db.Date, nullable=False)