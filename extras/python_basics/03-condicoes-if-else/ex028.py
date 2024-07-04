cores = {'limpa': '\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'roxo':'\033[34m'}
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('{}MULTADO! Você excedeu o limite permitido que é de 80Km/h.{}'.format(cores['vermelho'],cores['limpa']))
    multa = (velocidade - 80) * 7
    print('{}Você deve pagar uma multa de R${:.2f}!{}'.format(cores['roxo'], multa, cores['limpa']))
else:
    print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores['verde'], cores['limpa']))