# Cria janela vazia com loop do jogo #

import pygame
from pygame.locals import *

#Define a movimentação da cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) #CorBranca

direcao = LEFT

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            #Seta
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_LEFT:
                direcao = LEFT
            if event.key == K_RIGHT:
                direcao = RIGHT
                
    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
        if direcao == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if direcao == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if direcao == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if direcao == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
            
    screen.fill((0,0,0))
    for pos in snake:
        screen.blit(snake_skin,pos)
    pygame.display.update()