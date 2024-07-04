import pygame
print('Enjoy the sound! :D')
pygame.init()
pygame.mixer.music.load('ex020.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()