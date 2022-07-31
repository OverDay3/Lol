WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

def paintOnMonitor(sc, x1, y1, l, h, x2, y2, WIN_WIDTH, pr, r, pygame, x, y):
    sc.fill((0,0,0))
    pygame.draw.rect(sc, WHITE, 
                     (x1, y1, l, h)) 
    pygame.draw.rect(sc, WHITE, 
                     (x2, y2, WIN_WIDTH - l - pr , h))    
    pygame.draw.circle(sc, ORANGE,
                       (x, y), r)
