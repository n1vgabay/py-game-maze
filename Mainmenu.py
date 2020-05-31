import sys
sys.path.append('C:/Users/nivga/Documents/Coding/Python/pyGameTest')
import beans
import pygame
from beans.Player import *
from beans.Enemy import *
from beans.Bullet import *

red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

def button(msg,x,y,w,h,ic,ac,screen):
    gameDisplay =screen
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf = text_object_surf(msg, smallText)
    textRect = text_object_rect(textSurf)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def text_object_surf(text,textSurf):
    return textSurf.render(text,True,(0,0,0))

def text_object_rect(textSurf):
    textRect = textSurf.get_rect()
    return textRect


def MainUI(screen,width,height):
    pygame.init()
    screen.fill((210,210,210))
    #print("here Game Over")

    fontTitle = pygame.font.Font(None, 57)
    textTitle = fontTitle.render("Chickens Invaders",True,(255,0,0))
    textTitleRect = textTitle.get_rect()
    textTitleRect.center=(width/2,(height/2-300)+10)
    screen.blit(textTitle, textTitleRect)
    #button = pygame.Rect(width/2 -150, height/2+100, 300, 50)
    #pygame.draw.rect(screen, [255, 0, 0], button)
    pygame.mouse.set_visible(1)
    trig = True
    startTrig = False

    while trig:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                trig = False

        mouse = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        button("New Game",(width/2 -150),(height/2),300,50,green,bright_green,screen)
        button("Quit",(width/2 -150),(height/2+100),300,50,green,bright_green,screen)




        if (width/2 -150)+300 > mouse[0] > (width/2 -150) and (height/2)+50 > mouse[1] > (height/2) and pressed == (1,0,0):  
            startTrig = True
            trig = False
            
        elif (width/2 -150)+300 > mouse[0] > (width/2 -150) and (height/2+100)+50 > mouse[1] > (height/2) and pressed == (1,0,0):  
            pygame.quit()
        

        pygame.display.update()
        #pygame.time.Clock().tick(0)
    return startTrig
    pygame.quit()