import pygame
import time
pygame.init()
size = [1, 1]
screen = pygame.display.set_mode(size)
###bg_img = pygame.image.load('bg.png')

###zut = pygame.image.load('z.png')
###crv = pygame.image.load('c.png')

l = [0, 0, 0, 0, 0, 0, 0]
mat = []
for i in range(6):
    aaa = []
    for j in range(7):
        aaa.append(0)
    mat.append(aaa)

s = [6, 6, 6, 6, 6, 6, 6]
xstart = 120
ystart = 25
xc = xstart
yc = ystart

px = 0

red = 1

def output(red, r, s):
    pygame.display.flip()
    screen.blit(bg_img, (0, 0))
    screen.blit(crv, (120+r*125, 180+s*100))
    time.sleep(1)
    ###screen.blit(crv, (xc, yc))
    ###screen.blit(zut, (850, 180))


running = True
while running:

    ## provjera pobjede
    # u stupcu
    for i in range(6):
        for j in range(3):
            if mat[i][j] == 1 and mat[i][j+1] == 1 and mat[i][j+2] == 1 and mat[i][j+3] == 1:
                pygame.quit()
            if mat[i][j] == 2 and mat[i][j+1] == 2 and mat[i][j+2] == 2 and mat[i][j+3] == 2:
                pygame.quit()

    # u redu
    for i in range(7):
        for j in range(3):
            if mat[j][i] == 1 and mat[j+1][i] == 1 and mat[j+2][i] == 1 and mat[j+3][i] == 1:
                pygame.quit()
            if mat[j][i] == 2 and mat[j+1][i] == 2 and mat[j+2][i] == 2 and mat[j+3][i] == 2:
                pygame.quit()

    # dijagonalno   
    for i in range(3):
        for j in range(4):
            if mat[i][j] == 1 and mat[i+1][j+1] == 1 and mat[i+2][j+2] == 1 and mat[i+3][j+3] == 1:
                pygame.quit()
            if mat[i][j] == 2 and mat[i+1][j+1] == 2 and mat[i+2][j+2] == 2 and mat[i+3][j+3] == 2:
                pygame.quit()

                
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            l[px] = 0
            if event.key == pygame.K_LEFT and px > 0:
                px -= 1
            if event.key == pygame.K_RIGHT and px < 6:
                px += 1
            l[px] = red
            print('list', l, 's[px] = ', s[px])
            if event.key == pygame.K_DOWN and s[px] > 0:
                if s[px] > 1:
                    for i in range(1, s[px]):
                        mat[i][px] = red
                        mat[i-1][px] = 0
                    
                        for j in range(6):
                            print(mat[j])
                        print(s[px])
                        print('\n ---------- \n')
                
                else:
                    s[px] = 0
                    mat[0][px] = red
                    
                    
                    for j in range(6):
                        print(mat[j])
                    print(s[px])
                    print('\n ---------- \n')

                print('------------------------------------------')
                s[px] -= 1 
                    
                
                if red == 2:
                    red = 1
                else:
                    red = 2
            

                
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
    
