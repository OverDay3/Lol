def paintOnMonitor(sc, x1, y1, l, h, x2, y2, WIN_WIDTH, pr, ORANGE, r, pygame, x, y):
    sc.fill((0,0,0))
    pygame.draw.rect(sc, (255, 255, 255), 
                     (x1, y1, l, h)) 
    pygame.draw.rect(sc, (255, 255, 255), 
                     (x2, y2, WIN_WIDTH - l - pr , h))    
    pygame.draw.circle(sc, ORANGE,
                       (x, y), r)