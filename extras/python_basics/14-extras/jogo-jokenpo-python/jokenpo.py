from random import randint
from time import sleep
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
cores = {'limpa': '\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'roxo':'\033[34m',
         'azul':'\033[36m'}
itens = ('Pedra', 'Papel', 'Tesoura')
jogo = 1
nome = str(input('{}Olá, jogador! Digite seu nome: {}'.format(cores['roxo'], cores['limpa'])))
while jogo == 1:
    print('''Escolha sua jogada:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
    jogador = int(input('{}Qual é a sua jogada? {}'.format(cores['roxo'], cores['limpa'])))
    computador = randint(0, 2)
    pygame.init()
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play()
    print('{}Computador está pensando...{}'.format(cores['vermelho'], cores['limpa']))
    sleep(5)
    print('{}JO!{}'.format(cores['azul'], cores['limpa']))
    sleep(1.5)
    print('{}KEN!{}'.format(cores['azul'], cores['limpa']))
    sleep(1)
    print('{}PO!{}'.format(cores['azul'], cores['limpa']))
    sleep(1.5)
    print('-=' * 11)
    print('{}{}{} jogou {}{}{}!'.format(cores['verde'], nome, cores['limpa'], cores['verde'], itens[jogador], cores['limpa']))
    print('{}Computador{} jogou {}{}{}!'.format(cores['vermelho'], cores['limpa'], cores['vermelho'], itens[computador], cores['limpa']))
    print('-=' * 11)
    if jogador == 0: # jogador jogou PEDRA
        if computador == 0:
            print('{}EMPATE!{}'.format(cores['roxo'], cores['limpa']))
        elif computador == 1:
            print('Você {}PERDEU!{}'.format(cores['vermelho'], cores['limpa']))
        elif computador == 2:
            print('Você {}GANHOU!{}'.format(cores['verde'], cores['limpa']))
                
    elif jogador == 1: # jogador jogou PAPEL
        if computador == 0:
            print('Você {}GANHOU!{}'.format(cores['verde'], cores['limpa']))
        elif computador == 1:
            print('{}EMPATE!{}'.format(cores['roxo'], cores['limpa']))
        elif computador == 2:
            print('Você {}PERDEU!{}'.format(cores['vermelho'], cores['limpa'])) 
    elif jogador == 2: # jogador jogou TESOURA
        if computador == 0:
            print('Você {}PERDEU!{}'.format(cores['vermelho'], cores['limpa']))
        elif computador == 1:
            print('Você {}GANHOU!{}'.format(cores['verde'], cores['limpa']))
        elif computador == 2:
            print('{}EMPATE!{}'.format(cores['roxo'], cores['limpa']))
    else:
        print('{}Jogada inválida!{}'.format(cores['roxo'], cores['limpa']))
    print('''Escolha uma opção:
[ 0 ] SAIR
[ 1 ] CONTINUAR''')
    jogo = int(input('[   ]: '))
print('{}Jogo finalizado! Até a próxima! ;){}'.format(cores['roxo'], cores['limpa']))
        