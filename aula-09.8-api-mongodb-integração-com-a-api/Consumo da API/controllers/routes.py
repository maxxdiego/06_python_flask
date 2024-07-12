from flask import render_template, request
import urllib
import json

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/apigames', methods=['GET', 'POST'])
    def apigames():
        url = 'http://localhost:5000/games'
        res = urllib.request.urlopen(url)
        data = res.read()
        gamesjson = json.loads(data)
        return render_template('apigames.html', gamesjson=gamesjson)