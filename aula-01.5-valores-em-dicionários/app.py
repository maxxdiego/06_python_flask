from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    game = {'Título' : 'CS-GO', 
             'Ano' : 2012,
             'Categoria' : 'FPS Online'}
    jogadores = ['Pedro', 'João', 'Marcos', 'Maria']
    return render_template('games.html',
                           game=game,
                           jogadores=jogadores)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) 