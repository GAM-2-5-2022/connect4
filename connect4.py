import pygame
pygame.init()
size = [1100, 1000]
screen = pygame.display.set_mode(size)
bg_img = pygame.image.load('bg.png')

zut = pygame.image.load('z.png')
crv = pygame.image.load('c.png')

mat = []
for i in range(6):
    aaa = []
    for j in range(7):
        aaa.append(0)
    mat.append(aaa)

print(mat)

running = True
while running:
    pygame.display.flip()
    screen.blit(bg_img, (0, 0))
    screen.blit(crv, (50, 50))
    screen.blit(zut, (850, 180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
    
