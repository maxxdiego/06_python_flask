from api import app, mongo
from api.models.game_model import Game
from api.services import game_service

if __name__ == "__main__":
    with app.app_context():
        if 'games' not in mongo.db.list_collection_names():
            game = Game(
                titulo='',
                ano=0,
                descricao={
                    'genero': '',
                    'plataforma': '',
                    'classificacao': ''
                    }
                )
            game_service.add_game(game)
    app.run(debug=True)
