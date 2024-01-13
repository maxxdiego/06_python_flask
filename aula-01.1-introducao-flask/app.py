from flask import Flask #Importando a biblioteca Flask

app = Flask(__name__) #Carregando o Flask no objeto app

@app.route('/') #Definindo a rota principal '/'
def home(): #Função que será executada ao acessar a rota
    return '<h1>Esta é a Homepage!</h1>' #Retorno que será exibido

if __name__ == '__main__': #SE for executado diretamente pelo interpretador
    app.run(host='localhost', port=5000, debug=True) #Roda a aplicação em localhost:5000, com o modo debug ativado.'