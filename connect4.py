import pygame
import time
import sys
pygame.init()

def updateq():
    pygame.display.flip()
    screen.blit(pra, (0, 0))
    for i in range(7):
        if l[i] == 1:
            screen.blit(crv, (matq[i], 25))
        if l[i] == 2:
            screen.blit(zut, (matq[i], 25))
            
    pygame.display.update()
            
def update():
    pygame.display.flip()
    screen.blit(bg_img, (0, 0))
    for i in range(6):
        for j in range(7):
            if mat[i][j] == 1:
                screen.blit(crv, (matcord[i][j][0], matcord[i][j][1]))
            if mat[i][j] == 2:
                screen.blit(zut, (matcord[i][j][0], matcord[i][j][1]))
    time.sleep(0.2)
    

bg_img = pygame.image.load('bg2.png')
start_img = pygame.image.load('start.png')
zut = pygame.image.load('z.png')
crv = pygame.image.load('c.png')
zutpob = pygame.image.load('zuti.png')
crvpob = pygame.image.load('crveni.png')
pra = pygame.image.load('prazno.png')


size = [1100, 1000]
screen = pygame.display.set_mode(size)
pygame.display.flip()
screen.blit(start_img, (0, 0))
pygame.display.update()


s = [6, 6, 6, 6, 6, 6, 6]
xc = 120
yc = 25
px = 0
red = 1
pob = 0
mat = []
for i in range(6):
    aaa = []
    for j in range(7):
        aaa.append(0)
    mat.append(aaa)
matq = [120, 241, 362, 483, 604, 725, 846]
matcord = [[[120, 180],[245, 180],[365, 180],[490, 180],[610, 180],[730, 180],[850, 180]],
           [[120, 280],[245, 280],[365, 280],[490, 280],[610, 280],[730, 280],[850, 280]],
           [[120, 380],[245, 380],[365, 380],[490, 380],[610, 380],[730, 380],[850, 380]],
           [[120, 480],[245, 480],[365, 480],[490, 480],[610, 480],[730, 480],[850, 480]],
           [[120, 580],[245, 580],[365, 580],[490, 580],[610, 580],[730, 580],[850, 580]],
           [[125, 675],[245, 675],[365, 675],[490, 675],[610, 675],[730, 675],[850, 675]]]
   


## quit button
color_light = (170,170,170)
color_dark = (100,100,100)
width = 350
height = 700
smallfont = pygame.font.SysFont('Corbel', 50)
text = smallfont.render('QUIT' , True , (255,255,255))


## start button
color_light2 = (170,170,170)
color_dark2 = (100,100,100)
width2 = 350
height2 = 350
smallfont2 = pygame.font.SysFont('Corbel', 50)
text2 = smallfont2.render('START' , True , (255,255,255))

start = True

while start:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width <= mouse[0] <= width+350 and height <= mouse[1] <= height+75:
                pygame.quit()
            if width2 <= mouse[0] <= width2+350 and height2 <= mouse[1] <= height2+75:
                start = False
                running = True
        
            
    mouse = pygame.mouse.get_pos()
    
    if width <= mouse[0] <= width+350 and height <= mouse[1] <= height+75:
        pygame.draw.rect(screen,color_light,[width,height,350,75])
    else:
        pygame.draw.rect(screen,color_dark,[width,height,350,75])

    if width2 <= mouse[0] <= width2+350 and height2 <= mouse[1] <= height2+75:
        pygame.draw.rect(screen,color_light2,[width2,height2,350,75])
    else:
        pygame.draw.rect(screen,color_dark2,[width2,height2,350,75])
        
    screen.blit(text , (width+120,height+15))
    screen.blit(text2 , (width2+106,height2+15))
    pygame.display.update()

    
    
screen = pygame.display.set_mode(size)
pygame.display.flip()
screen.blit(bg_img, (0, 0))
pygame.display.update()

l = [1, 0, 0, 0, 0, 0, 0]
updateq()
l = [0, 0, 0, 0, 0, 0, 0]

while running:
    
    ## provjera pobjede
    # u stupcu
    for i in range(6):
        for j in range(3):
            if mat[i][j] == 1 and mat[i][j+1] == 1 and mat[i][j+2] == 1 and mat[i][j+3] == 1:
                running = False
                pob = 1
            if mat[i][j] == 2 and mat[i][j+1] == 2 and mat[i][j+2] == 2 and mat[i][j+3] == 2:
                running = False
                pob = 2

    # u redu
    for i in range(7):
        for j in range(3):
            if mat[j][i] == 1 and mat[j+1][i] == 1 and mat[j+2][i] == 1 and mat[j+3][i] == 1:
                running = False
                pob = 1
            if mat[j][i] == 2 and mat[j+1][i] == 2 and mat[j+2][i] == 2 and mat[j+3][i] == 2:
                running = False
                pob = 2

    # dijagonalno   
    for i in range(3):
        for j in range(4):
            if mat[i][j] == 1 and mat[i+1][j+1] == 1 and mat[i+2][j+2] == 1 and mat[i+3][j+3] == 1:
                running = False
                pob = 1
            if mat[i][j] == 2 and mat[i+1][j+1] == 2 and mat[i+2][j+2] == 2 and mat[i+3][j+3] == 2:
                running = False
                pob = 2

    # dijagonalno2 
    for i in range(5, 2, -1):
        for j in range(4):
            if mat[i][j] == 1 and mat[i-1][j+1] == 1 and mat[i-2][j+2] == 1 and mat[i-3][j+3] == 1:
                running = False
                pob = 1
            if mat[i][j] == 2 and mat[i-1][j+1] == 2 and mat[i-2][j+2] == 2 and mat[i-3][j+3] == 2:
                running = False
                pob = 2
                
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            l[px] = 0
            if event.key == pygame.K_LEFT and px > 0:
                px -= 1
            if event.key == pygame.K_RIGHT and px < 6:
                px += 1
            l[px] = red
            updateq()
            
            '''
            print('list', l, 's[px] = ', s[px])
            '''
            
            if event.key == pygame.K_DOWN and s[px] > 0:
                if s[px] > 1:
                    mat[0][px] = red
                    update()
                    for i in range(1, s[px]):
                        mat[i][px] = red
                        mat[i-1][px] = 0

                        update()
                        
                        '''
                        for j in range(6):
                            print(mat[j])
                        print(s[px])
                        print('\n ---------- \n')
                        '''
                
                else:
                    s[px] = 0
                    mat[0][px] = red
                    
                    update()
                    
                    '''
                    for j in range(6):
                        print(mat[j])
                    print(s[px])
                    print('\n ---------- \n')

                print('------------------------------------------')
                '''
                    
                s[px] -= 1 
                    
                
                if red == 2:
                    red = 1
                    l = [1, 0, 0, 0, 0, 0, 0]
                    updateq()
                    l = [0, 0, 0, 0, 0, 0, 0]
                    px = 0
                else:
                    red = 2
                    l = [2, 0, 0, 0, 0, 0, 0]
                    updateq()
                    l = [0, 0, 0, 0, 0, 0, 0]
                    px = 0
                update()

                
        if event.type == pygame.QUIT:
            running = False

if pob == 1:
    screen.blit(crvpob, (350, 200))
    pygame.display.update()
    time.sleep(5)
elif pob == 2:
    screen.blit(zutpob, (350, 200))
    pygame.display.update()
    time.sleep(5)
pygame.quit()



    
