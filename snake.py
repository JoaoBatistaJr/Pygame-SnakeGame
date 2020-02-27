import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

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
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) #corBranca

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #corVermelho

#Direções
direcao = LEFT

#Limite de FPS
clock = pygame.time.Clock()

#fonte e placar
font = pygame.font.Font('freesansbold.ttf', 20)
score = 0

#Loop do game.
game_over = False
while not game_over:
    clock.tick(10)#Velocidade da snake
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() 
                
        #Mapeamento do teclado
        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            if event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            if event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
            if event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT
                
    #Teste de colisões
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
        
    #Colisão com as paredes
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    #Colisão da snake com ela mesma.
    for i in range(1, len(snake) -1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break
        
    
    
    if game_over:
        break
    
    #Colisão com a maçã
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])  
                
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
    
    #Desenha o grid
    for x in range(0, 600, 10): #Linhas horizontais
        pygame.draw.line(screen, (40,40,40), (x,0), (x, 600))
    for y in range(0, 600, 10): #Linhas verticais
        pygame.draw.line(screen, (40,40,40), (0,y), (600,y))
        
    #Desenha o placar
    score_font = font.render('Score: %s' %(score), True, (255,255,255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    for pos in snake:
        #Desenha a snake na tela
        screen.blit(snake_skin,pos)   
             
    #Renderiza o jogo          
    pygame.display.update()
    
while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75) 
    game_over_screen = game_over_font.render('Game Over', True, (255,255,255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.displayx.update()
    pygame.time.wait(500)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()