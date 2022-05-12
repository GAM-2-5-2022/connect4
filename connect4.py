import pygame
pygame.init()


screen = pygame.display.set_mode((400,550))
background = pygame.image.load('connect-four-bg.jpg')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255, 0, 0))
    pygame.display.update()
