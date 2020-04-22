import pygame
from pygame.locals import *

pygame.init()



r = 255
g = 0
b = 0

windown = pygame.display.set_mode((1500,1500))



pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

windown_open = True
pygame.font.init()

txt = "Color".format(r,g,b)

fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 60)


while windown_open:
    pygame.display.flip()



    txttela = fontesys.render(txt, 1, (r,g,b))
    windown.blit(txttela,(0,0))



    mouse = pygame.mouse.get_pos()
    comand = pygame.key.get_pressed()
    clock.tick(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windown_open = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(windown, (r,g,b), (mouse),30)

    if comand[pygame.K_F1] and r < 255:
        r+=1

    if comand[pygame.K_F2] and g < 255:
        g+=1


    if comand[pygame.K_F3] and b < 255:
        b+=1


    if comand[pygame.K_F4] and r > 1:
        r-=1


    if comand[pygame.K_F5] and r > 1:
        g-=1


    if comand[pygame.K_F6] and r > 1:
        b-=1


    #pygame.display.update()
pygame.quit()
