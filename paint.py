import pygame

pygame.init()
x = 400
y = 300

Speed = 5


windown = pygame.display.set_mode((1800,1600))

pygame.display.set_caption("Carrinho")

clock = pygame.time.Clock()

windown_open = True
while windown_open:
    comand = pygame.mouse.get_pos()
    clock.tick(1000)
    #windown.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windown_open = False
            




    pygame.draw.circle(windown, (50,100,25), (comand),25)
    pygame.display.update()
pygame.quit()
