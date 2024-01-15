import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600
line_width = 2

clicked = False
player=1
game_over = [False]

markers = []
for i in range(3):
    row=[0]*3
    markers.append(row)

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("triki")

def draw_grid():
    bg=(117,255,51)
    grid = (0,0,0)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen,grid,(0,x*200),(screen_width,x*200),line_width)
        pygame.draw.line(screen,grid,(x*200,0),(x*200,screen_width),line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y==1:
                pygame.draw.circle(screen,(0,0,0),(x_pos*200+100,y_pos*200+100),50)
            if y==-1:
                pygame.draw.circle(screen,(255,255,255),(x_pos*200+100,y_pos*200+100),50)
            y_pos +=1
        x_pos += 1

def verify():
    for i in  range(0,3) :
        if markers[0][i]==markers[1][i] and markers[0][i]==markers[2][i] and markers[0][i]!=0:
            game_over[0]=True 
            if markers[0][i]==-1:
                print("gana blanco")
            elif markers[0][i]==1:
                print("gana color asaltante")

    for i in  range(0,3) :
        if markers[i][0]==markers[i][1] and markers[i][0]==markers[i][2] and markers[i][0]!=0:
            if markers[i][0]==-1:
                print("gana blanco")
            elif markers[i][0]==1:
                print("gana color asaltante")
            game_over[0]=True 

    if markers[0][0]==markers[1][1] and markers[0][0]==markers[2][2] and markers[0][0]!=0:
        if markers[0][0]==-1:
             print("gana blanco en diagonal izquierdo")
        elif markers[0][0]==1:
            print("gana color asaltante en diagonal izquierdo")
            game_over[0]=True 

    if markers[0][2]==markers[1][1] and markers[0][2]==markers[2][0] and markers[0][2]!=0:
        if markers[0][2]==-1:
             print("gana blanco en diagonal derecho")
        elif markers[0][2]==1:
            print("gana color asaltante en diagonal derecho")
            game_over[0]=True 
    

    

run = True
while run:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked==False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked==True and game_over[0]!=True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]//200
            cell_y = pos[1]//200
            if markers[cell_x][cell_y]==0:
                markers[cell_x][cell_y]=player
                player=player*-1

            verify()

                    
                    

    pygame.display.update()

pygame.quit()

    


# print(markers)




