import pygame
import sys, random
sys.path.append('C:/Users/nivga/Documents/Coding/Python/pyGameTest')
import beans
import assets
from assets import *
from main.Gameover import * 
from main.Mainmenu import *
from beans.Player import *
from beans.Enemy import *
from beans.Bullet import *


# Notes:
#  New weapons
#  Change enemy creation algorithm
#  Create more enemies
#  Falling hearts and weapons
#  Find a niche
#  Build 3 stages at least










pygame.init()
pygame.font.init()
player = None
enemies_list = None
bullets = None
width, height  = 1000, 960
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
image_lib = ['fullheart.png','halfheart.png']

def lifeDamage(damage):
    if player.life > 0 and player.lifeDelay == 0:
        player.life -= damage
        player.lifeDelay = 1

def blinkWhileTakeDamage():
    if player.lifeDelay > 0:
        player.lifeDelay += 1
        if player.lifeDelay % 10 == 0:
            player.image.fill((255,255,255))
        else :
            player.image.fill((255,0,0))
    if player.lifeDelay > 70:    
        player.lifeDelay = 0
        player.image.fill((255,0,0))

def lifeToHearts():
    pass
    ind = 0
    for i in range(1,player.life+1,1):
        if i % 2 == 0:
            img = pygame.image.load(".\\pyGameTest\\assets\\fullheart.png")
            img.convert()
            rect = img.get_rect()
            rect.topleft= ((50 + ind,50))
            ind += 60
            pygame.draw.rect(screen, (255,255,255), rect, 1)
            screen.blit(img, rect)
            pygame.display.update()
        elif(i % 2 != 0 and i == player.life):
            
            img = pygame.image.load(".\\pyGameTest\\assets\\halfheart.png")
            img.convert()
            rect = img.get_rect()
            rect.topleft= ((50 + ind,50))
            ind += 60
            pygame.draw.rect(screen, (255,255,255), rect, 1)
            screen.blit(img, rect)
            pygame.display.update()
            
# Blink function when there is interaction between player and evemy
# when life.delay modulo is 0, color'll change to white and the next iteration color will be red again
# until we reach life.delay of 0 again
# which restarts our life.delay value to zero again (no collision then, so no blink function is running) 


def checkGameOver():
    if player.life <= 0:
        # return true if game is over
        startnewgame = gameOver(player,screen,width,height)
        if startnewgame :
            for e in enemies_list:
               enemies_list.remove(e)
            for b in bullets:
               bullets.remove(b)
        newGame()
        startnewgame = False
       

# Define player possitions via the player class constructor using mouse x/y
def setPlayerPos(x, y):
    player.x = x
    player.y = y
    player.rect.x = x
    player.rect.y = y
    if player.x > width - player.width:
        player.x = width - player.width
    elif player.x < 0:
        player.x = 0
    if player.y > height - player.height:
        player.y = height - player.height
    elif player.y < 0:
        player.y = 0

# Function collision between player with enemy
def colPlayer():
    for enemy in enemies_list:
        enemy.y += 5
        enemy.rect.y = enemy.y
        enemy.draw(screen)
        if enemy.y > height + 200:
            enemies_list.remove(enemy)    
    if pygame.sprite.spritecollide(player, enemies_list, False) :   
        lifeDamage((enemy.damage))
        
        

# Function collision between bullet with enemy
def colBullet():
    for enemy in enemies_list:
        for bullet in bullets:
            if bullet.y-3 <= enemy.y + enemy.height and bullet.y-3 >= (enemy.y + enemy.height)-10 and ((bullet.x >= enemy.x and 
                bullet.x-3 <= enemy.x + enemy.width)):
                        enemy.life -= bullet.damage
                        bullet.damage = 0
                        bullets.remove(bullet)
                        enemy.removeEnemyNoLife(enemies_list, player)
     

def window():
    player.draw(screen)
    #screen.blit(textLife, textLifeRect)
    screen.blit(textScore, textScoreRect)
    lifeToHearts()
        
    




def newGame():
    pygame.init()
    pygame.font.init()
    width, height  = 1000, 960
    screen = pygame.display.set_mode((width,height))
    player.life = 6
    player.score = 0
    speed = 9
    shootDelay = 0
    enemies_list = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemy_creation_timming = 0
    shotTrig = True
    pygame.mouse.set_visible(0)


startnewgame = False

# Main loop/ Game loop
run = True
startnewgame = MainUI(screen,width,height)
while run:
    if startnewgame:
        player = Player(225,400,(255,0,0))
        player.life = 6
        player.score = 0
        speed = 9
        shootDelay = 0
        enemies_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        enemy_creation_timming = 0
        shotTrig = True
        pygame.mouse.set_visible(0)
        startnewgame = False
        lifeToHearts()


    


        

    #fontLife = pygame.font.Font(None, 40)
    #textLife = fontLife.render("Life: " + str(player.life),True,(0,128,0))
    fontScore = pygame.font.Font(None, 40)
    textScore = fontScore.render("Score: " + str(player.score),True,(0,128,0))
    #textLifeRect = textLife.get_rect()
    #textLifeRect.topleft= ((50,50))
    textScoreRect = textScore.get_rect()
    textScoreRect.topleft= (((width - 200), 50))
    #screen.blit(textLife, textLifeRect)
    screen.blit(textScore, textScoreRect)

    if shootDelay > 0:
        shootDelay += 1
    if shootDelay > 10:    
        shootDelay = 0

    blinkWhileTakeDamage()

    shotTrig = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

      
    mousex = pygame.mouse.get_pos()[0]
    mousey = pygame.mouse.get_pos()[1]
    setPlayerPos(mousex,mousey)

    checkGameOver()
  
    
    if  (pygame.mouse.get_pressed()[0]) == 1 and shootDelay == 0 :
        bullets.add(Bullet(round(player.x + player.width//2), round(player.y + player.height//2), 6, (0,0,0) ))
        shootDelay = 1


    # Creating enemies
    enemy_creation_timming += 1
    if enemy_creation_timming == 30:
        enemy_creation_timming = 0
        new_enemy = Enemy(random.randint(10, width - player.width), -50, (0,255,0))
        enemies_list.add(new_enemy)
        new_enemy.draw(screen)

    screen.fill((255,255,255))

    # show bullets on screen + control speed
    for bullet in bullets:
        bullet.y -= bullet.speed
        bullet.draw(screen)
        if bullet.y < 0:
            bullets.remove(bullet)

    # Call collision function (bullet with enemy)
    colBullet()
    # Call collision function (player with enemy)
    colPlayer()

    # Redraw screen 
    window()
    pygame.display.update()

    # Frame per second, affects the speed of the game
    clock.tick(40) # FPS
pygame.quit()