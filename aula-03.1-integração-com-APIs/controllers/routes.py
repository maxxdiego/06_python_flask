from flask import render_template, request
import urllib
import json

jogadores = []
gamelist = [{'Título' : 'CS-GO', 'Ano' : 2012, 'Categoria' : 'FPS Online'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html',
                                game=game,
                                jogadores=jogadores)
        
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
        
        return render_template('cadgames.html',
                                gamelist=gamelist)
    
    @app.route('/apigames', methods=['GET', 'POST'])
    def apigames():
        url = 'https://www.freetogame.com/api/games'
        res = urllib.request.urlopen(url)
        data = res.read()
        gamesjson = json.loads(data)
        return render_template('apigames.html', gamesjson=gamesjson)