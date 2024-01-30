from flask import Flask, render_template
from controllers import routes
from models.database import db
import os

app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Permite ler o diretório absoluto de um determinado arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Passando o diretório do banco ao SQLAlchemy 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')

# Secret para as flash messages
app.config['SECRET_KEY'] = 'thegamessecret'

# Define o tempo de duração da sessão
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

if __name__ == '__main__':
    # Verifica no início da aplicação se o BD já existe. Caso contrário ele criará o BD.
    db.init_app(app=app)
    # db.create_all()
    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=5000, debug=True) 