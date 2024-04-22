from flask import Flask, render_template
from controllers import routes
from models.database import db
import pymysql


app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Define o nome do banco de dados
DB_NAME = 'games'
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao SQLAlchemy 
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:admin@localhost/{DB_NAME}'

# Secret para as flash messages
app.config['SECRET_KEY'] = 'thegamessecret'
# Define o tempo de duração da sessão
app.config['PERMANENT_SESSION_LIFETIME'] = 1800
# Define pasta que receberá arquivos de upload
app.config['UPLOAD_FOLDER'] = 'static/uploads'
# Define o tamanho máximo de um arquivo de upload
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if __name__ == '__main__':
# Conecta ao MySQL para criar o banco de dados, se necessário
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='admin',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Cria o banco de dados se ele não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados está criado!")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()

    # Inicializa a aplicação Flask
    db.init_app(app=app)

    with app.test_request_context():
        # Cria as tabelas
        db.create_all()

    # Inicia o aplicativo Flask
    app.run(host='localhost', port=5000, debug=True)