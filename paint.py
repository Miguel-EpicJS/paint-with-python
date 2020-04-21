import pygame
from pygame.locals import *

pygame.init()



r = 255
g = 0
b = 0

windown = pygame.display.set_mode((1500,1500))

pygame.display.set_caption("Carrinho")

clock = pygame.time.Clock()

windown_open = True
pygame.font.init()




while windown_open:

    txtR = 'Red:  '
    txtG = 'Green: '
    txtB = 'Blue: '
    numR = '{}'.format(r)
    numG = '{}'.format(g)
    numB = '{}'.format(b)
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 60)
    txttelaR = fontesys.render(txtR, 1, (255,255,255))
    txttelaG = fontesys.render(txtG, 1, (255,255,255))
    txttelaB = fontesys.render(txtB, 1, (255,255,255))
    numtelaR = fontesys.render(numR, 1, (255,255,255))
    numtelaG = fontesys.render(numG, 1, (255,255,255))
    numtelaB = fontesys.render(numB, 1, (255,255,255))
    windown.blit(txttelaR,(0,0))
    windown.blit(txttelaG,(0,50))
    windown.blit(txttelaB,(0,100))
    windown.blit(numtelaR,(150,0))
    windown.blit(numtelaG,(150,50))
    windown.blit(numtelaB,(150,100))

    mouse = pygame.mouse.get_pos()
    comand = pygame.key.get_pressed()
    clock.tick(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windown_open = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(windown, (r,g,b), (mouse),25)

    if comand[pygame.K_F1] and r < 255:
        r+=1
        numtelaR = fontesys.render(numR, 1, (255,255,255))
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




    pygame.display.update()
pygame.quit()
