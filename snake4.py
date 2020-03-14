import pygame

from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Definição das cores
BRANCO = pygame.Color('white')
VERMELHO = pygame.Color('red')

#Metodo de inialialização
pygame.init()
screen = pygame.display.set_mode((540,480))
pygame.display.set_caption('Snake Game 4.0')

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()