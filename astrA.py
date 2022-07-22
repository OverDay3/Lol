import pygame
import sys
from pygame.locals import *
from random import randint

 
FPS = 60
WIN_WIDTH = 1600
WIN_HEIGHT = 900
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
r = 10
h = 50
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("LOL")


direction = False
pr = 50
x1 = 0
y1 = -h
l = randint(0, WIN_WIDTH-pr)

n = 1
x2 = l + pr
y2 = -h


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == KEYDOWN: direction = i.key # Other key pressed
        if i.type == KEYUP:  direction = False # Key released
    if direction:
        if direction == K_w:
            y-=5
        elif direction == K_s:
            y+=5
        elif direction == K_a:
            x-=5
        elif direction == K_d:
            x+=5
    sc.fill((0,0,0))
    pygame.draw.rect(sc, (255, 255, 255), 
                     (x1, y1, l, h)) 
    pygame.draw.rect(sc, (255, 255, 255), 
                     (x2, y2, WIN_WIDTH - l - pr , h))    
    pygame.draw.circle(sc, ORANGE,
                       (x, y), r)
    if x > WIN_WIDTH - r:
        x = WIN_WIDTH - r
    elif x < r:
        x = r
    elif y > WIN_HEIGHT - r:
        y = WIN_HEIGHT - r
    elif y < r:
        y = r
    y1 += 2 * n
    y2 += 2 * n
    if y1 >= WIN_WIDTH:
        y1, y2 = -h, -h
        l = randint(0, WIN_WIDTH-pr)
        n += 0.05
        
    pygame.display.update()
    
 
    clock.tick(FPS)
