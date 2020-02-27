import pygame, random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Método de inicialização
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

#Entidades
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255,255,255)) #corBranca

apple_pos = (random.randint(0, 590), random.randint(0, 590))
apple = pygame.Surface((10, 10))
apple.fill((255,0,0)) #corVermelho

#Direções
direcao = LEFT

#Loop do game.
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    #Mapeando as posições da snake
    if direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        
        
    #Limpa a tela
    screen.fill((0,0,0))
    #Desenha a apple na tela
    screen.blit(apple, apple_pos)
    
    
    for pos in snake:
        #Desenha a snake na tela
        screen.blit(snake_skin,pos)
            
 #Renderiza o jogo          
pygame.display.update()