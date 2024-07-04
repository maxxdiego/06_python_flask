from random import randint
from time import sleep
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
itens = ('Pedra', 'Papel', 'Tesoura')
jogo = 1
nome = str(input('Olá, jogador! Digite seu nome: '))
while jogo == 1:
    print('''Escolha sua jogada:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    computador = randint(0, 2)
    pygame.init()
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play()
    print('Computador está pensando...')
    sleep(5)
    print('JO!')
    sleep(1.5)
    print('KEN!')
    sleep(1)
    print('PO!')
    sleep(1.5)
    print('-=' * 11)
    print('{} jogou {}!'.format(nome, itens[jogador]))
    print('Computador jogou {}!'.format(itens[computador]))
    print('-=' * 11)
    if jogador == 0: # jogador jogou PEDRA
        if computador == 0:
            print('EMPATE!')
        elif computador == 1:
            print('Você PERDEU!')
        elif computador == 2:
            print('Você GANHOU!')
                
    elif jogador == 1: # jogador jogou PAPEL
        if computador == 0:
            print('Você GANHOU!')
        elif computador == 1:
            print('EMPATE!')
        elif computador == 2:
            print('Você PERDEU!')
    elif jogador == 2: # jogador jogou TESOURA
        if computador == 0:
            print('Você PERDEU!')
        elif computador == 1:
            print('Você GANHOU!')
        elif computador == 2:
            print('EMPATE!')
    else:
        print('Jogada inválida!')
    print('''Escolha uma opção:
[ 0 ] SAIR
[ 1 ] CONTINUAR''')
    jogo = int(input('[   ]: '))
print('Jogo finalizado! Até a próxima! ;)')
sleep(3)
        