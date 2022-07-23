import pygame
import sys
from pygame.locals import *
from random import randint
from playerMove import posX, posY
from monitor import paintOnMonitor

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 400
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

r = 10
h = 50

x = WIN_WIDTH // 2
y = WIN_HEIGHT - 40
 
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

move = [False, False, False, False]
playerSpeed = 3

while True:

    for i in pygame.event.get():
        tap = False
        if i.type == KEYDOWN: tap = True

        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if tap == True:
            if i.key == K_w: move[0] = True
            if i.key == K_s: move[1] = True
            if i.key == K_a: move[2] = True
            if i.key == K_d: move[3] = True
            if i.key == K_ESCAPE: exit(0)

        tap = False
        if i.type == KEYUP: tap = True

        if tap == True:
            if i.key == K_w: move[0] = False
            if i.key == K_s: move[1] = False
            if i.key == K_a: move[2] = False
            if i.key == K_d: move[3] = False
            if i.key == K_ESCAPE: exit(0)


    x = posX(x, move, playerSpeed)
    y = posY(y, move, playerSpeed)

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
        
    paintOnMonitor(sc, x1, y1, l, h, x2, y2, WIN_WIDTH, pr, ORANGE, r, pygame, x, y)
    pygame.display.update()
    
 
    clock.tick(FPS)
