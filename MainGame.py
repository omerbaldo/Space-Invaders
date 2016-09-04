import pygame
import sys
from pygame.locals import *
from Player import Player
from Enemy import Enemy


#-----------------------------------------------------------------------------------------Helper Methods


# Sets / Switches Background
def background(image, width, height):
    global screen
    global background
    screen = pygame.display.set_mode((width, height)) # how big it looks
    background = pygame.image.load(image).convert_alpha();

# Draws score and background
def scoreRender():
    # print out the score
        global score, score_text, score_rect
        score += 10
        score_text = font.render('Score: %s , Lives %d' % (score, player.lives), 1, (255, 255, 25))
        screen.blit(background, (0, 0))     # update the background
        screen.blit(score_text, score_rect) # put score text on score rectange

# Draws instructions and background
def instructionsRender():
    # print out the score
        global score_rect
        instructions = font.render('Press Enter to play again.', 1, (255, 255, 255))
        instructions_rect = score_rect

        screen.blit(background, (0, 0))
        screen.blit(instructions, instructions_rect)


#-------------------------------------------------------------------------------------------Set up
pygame.init()               # intitialize pygame modules
background("images/background.jpg",1240,826)
# 640 480


# Score Stuff
score = 0
font = pygame.font.SysFont(None, 36)

score_text = font.render('Score: %s' %(score), 1, (0, 0, 0)) #Score Rectangle
score_rect = score_text.get_rect()
score_rect.topleft = (50, 50)

state = 0 # state for menu, game, gameover ect.

screen.blit(background, (0, 0))            # draws background at origin
pygame.display.set_caption('Game Base')    # makes a captian of the window
font = pygame.font.SysFont(None, 36,True,True)       # creates a font object

player = Player() # Creates a player object

enemy = Enemy(500,100)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)
# Grouping sprites
all_group = pygame.sprite.Group()
all_group.add(player)
all_group.add(enemy)


main_clock = pygame.time.Clock()
direction = -1  # 0 is right, 1 is left


# -----------------------------------------------------------------------------------------Begin Game
while True:
    main_clock.tick(60) # 60 Frames A Second

    # check for events
    for event in pygame.event.get(): # these are signals sent from pygame
        if event.type == QUIT:       # if signal is quit, then exit
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()  # returns keys input

    # Eight Directional Movement
    '''
    Direction           Degree   Direction        
    0                        0            North
    1                        45          North East
    2                        90          East
    3                       135         South East
    4                       180         South
    5                       225         South West
    6                       270         West
    7                       315         North West 
    8                       360/0      North 

    '''
    if state == 0:
        if keys[K_w] and keys[K_d]: # north east 
            direction = 1
        elif keys[K_s] and keys[K_d]: # south east
            direction = 3
        elif keys[K_s] and keys[K_a]: # south west
            direction = 5
        elif keys[K_a] and keys[K_w]: # north west
            direction = 7
        elif keys[K_a]:
            direction = 6
        elif keys[K_d]:
            direction = 2
        elif keys[K_s]:
            direction = 4
        elif keys[K_w]:
            direction = 0
        elif keys[K_SPACE]:
            all_group = player.shoot(all_group)


        else:
            direction = -1
        # print direction


        collide_list = pygame.sprite.spritecollide(player, enemy_group, False, collided = None)
        if len(collide_list) > 0:
            player.subtract_lives()  # loose one life
            for enemy in collide_list:
                enemy.collision()    # call the collision method



        # print out the score
    
        scoreRender()
        player.update(direction) # call the player object with input
        enemy.update()



        all_group.clear(screen, background)
        all_group.draw(screen)
       

        if player.get_lives() <= 0:
            state = 1


    elif state == 1:
        if keys[K_RETURN]:
            score = 0
            player.set_lives(3)
            state = 0
            enemy.speed = 2
            player.rect.x = 100
            player.rect.y = 900
            enemy.rect.x = 200
            enemy.rect.y = 700

        instructionsRender()

    pygame.display.update()