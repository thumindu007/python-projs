import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1000, 500))
MOVE_DOWN = pygame.USEREVENT + 1
clock = pygame.time.Clock()
pygame.display.set_caption('falling red square')
timer = pygame.time.Clock()
pygame.time.set_timer(MOVE_DOWN, 30)
x = 500
redy = 100
redx = random.randrange(1,999)
score = 0

running = True  
while running:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x = x - 10
            elif event.key == pygame.K_d:
                x = x + 10
        if event.type == MOVE_DOWN:
            redy = redy + 1
        if redy > 500:
            redx = random.randrange(1,999)
            redy = 100
        if redy == 400 and x <= redx and x+100 >= redx:
            score = score + 1
            redy = 100
            redx = random.randrange(1,999)
            print(score)
    
    pygame.draw.rect(screen, 'red', (redx, redy, 10, 10))
    pygame.draw.rect(screen, 'black', (x, 400, 90, 10))
    
    pygame.display.update()
    timer.tick(90)