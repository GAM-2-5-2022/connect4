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
xc = 120
yc = 25

red = 0

running = True
while running:
    pygame.display.flip()
    screen.blit(bg_img, (0, 0))
    
    for event in pygame.event.get():
        if red == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xc -= 121
                if event.key == pygame.K_RIGHT:
                    xc += 121
                pygame.display.update()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xc -= 121
                if event.key == pygame.K_RIGHT:
                    xc += 121
                pygame.display.update()

                
        if event.type == pygame.QUIT:
            running = False

    if xc < 121:
        xc = 121
    if xc > 850:
        xc = 847

    screen.blit(crv, (xc, yc))
    screen.blit(zut, (850, 180))
    
pygame.quit()
    
