from flask import Flask, render_template
from controllers import routes
from models.database import mongo, Game

app = Flask(__name__, template_folder='views')
routes.init_app(app)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/games'

if __name__ == '__main__':
    mongo.init_app(app=app)
    # Adicione um documento à coleção ao iniciar o aplicativo
    with app.app_context():
        # Supondo que 'games' seja o nome da sua coleção
        if 'games' not in mongo.db.list_collection_names():
            # Insira um documento para criar a coleção
            game = Game(
                titulo='',
                ano=0,
                categoria='',
                plataforma='',
                preco=0,
                quantidade=0
            )
            game.save()
        
    app.run(host='localhost', port=5000, debug=True) 