from flask import render_template, request

jogadores = []

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        games = {'Título' : 'CS-GO', 
                'Ano' : 2012,
                'Categoria' : 'FPS Online'}
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html',
                                games=games,
                                jogadores=jogadores)