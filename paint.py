import pygame
from pygame.locals import *


pygame.init()
#Cores
r = 255
g = 0
b = 0
t = 30


windown = pygame.display.set_mode((1500,1500))#cria a sala



pygame.display.set_caption("Paint")#coloca um nome

clock = pygame.time.Clock()

windown_open = True
pygame.font.init()

txt = "Color".format(r,g,b)

fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 60)

x = 0
y = 0

while windown_open:
    
    x =pygame.mouse.get_pos(x)
    y =pygame.mouse.get_pos(y)


    txttela = fontesys.render(txt, 1, (r,g,b))
    windown.blit(txttela,(0,0))



    mouse = pygame.mouse.get_pos()
    comand = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windown_open = False

    if comand[pygame.K_c]:
        pygame.draw.circle(windown, (r,g,b), (mouse),t)

    if comand[pygame.K_l]:
        pygame.draw.line(windown, (r,g,b), (mouse), (mouse), t)


    if comand[pygame.K_e]:
        pygame.draw.circle(windown, (0,0,0), (mouse), t)


    if comand[pygame.K_KP_PLUS]:
        t +=1
    if comand[pygame.K_KP_MINUS] and t >= 2:
        t -=1

    if comand[pygame.K_KP1] and r < 255:
        r+=1

    if comand[pygame.K_KP2] and g < 255:
        g+=1


    if comand[pygame.K_KP3] and b < 255:
        b+=1


    if comand[pygame.K_KP4] and r > 1:
        r-=1


    if comand[pygame.K_KP5] and r > 1:
        g-=1


    if comand[pygame.K_KP6] and r > 1:
        b-=1


    pygame.display.update()
pygame.quit()

