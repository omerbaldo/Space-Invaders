import pygame
import random
class Enemy(pygame.sprite.Sprite): # inherits from this class

    def __init__(self, x, y): #initialization, takes itsself as an arguement
        super(Enemy, self).__init__()
        self.image = pygame.image.load("images/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y)) # this is where the enemy will be initialized
        self.direction = 0
        self.speed = 2
    # if it goes out of screen, increase speed and go in new direction
    def boundsCheck(self):
        if self.rect.x > 1240 or self.rect.x < 0:
            self.rect.x = 600
            self.rect.y = 600
            self.direction = random.randint(0,7)
            self.speed +=1
        elif self.rect.y > 826 or self.rect.y < 0:
            self.rect.x = 600
            self.rect.y = 600
            self.direction = random.randint(0,7)
            self.speed += 1

    def update(self):
        print "direction is %s" % (self.direction)
        self.boundsCheck()
        if self.direction == 0:
            self.rect.y -= self.speed
            # good

        elif self.direction == 1:
            #good
            self.rect.x += self.speed
            self.rect.y -= self.speed

        elif self.direction == 2:
            #good
            self.rect.x += self.speed

        elif self.direction == 3:
            #good
            self.rect.x += self.speed
            self.rect.y += self.speed

        elif self.direction == 4:
            #good
            self.rect.y += self.speed

        elif self.direction == 5:
            #good
            self.rect.x -= self.speed
            self.rect.y += self.speed

        elif self.direction == 6:
            #good
            self.rect.x -= self.speed

        elif self.direction == 7:
            #good
            self.rect.x -= self.speed
            self.rect.y -= self.speed

    def collision(self): # go back to the top
        self.rect.y = 0