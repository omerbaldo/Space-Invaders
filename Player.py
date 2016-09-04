import pygame
from Bullet import Bullet
class Player(pygame.sprite.Sprite): # inherits from the pygame sprite class

    def __init__(self):#initialization, takes itsself as an arguement
        super(Player,self).__init__() # initializes parent class
    
        self.image = pygame.image.load("images/player1.png").convert_alpha()
        self.rect = self.image.get_rect(center=(300, 380)) # init x and y
        self.lives = 3
        self.initial_rotation = 0
        self.ship_image_list = []
        self.rotateImages()
        self.speed = 30
        self.bullet_list = []
        self.direction = -1
        #rotateImages() # get eight images for rotation 

    def update(self, direction):
        #print "player direction %d " % self.direction
        if direction != -1:
            self.direction = direction
        if direction == 0:
            self.rect.y -= self.speed
            self.image =  self.ship_image_list[0]
            # good

        elif direction == 1:
            #good
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.image =  self.ship_image_list[7]

        elif direction == 2:
            #good
            self.rect.x += self.speed
            self.image =  self.ship_image_list[6]

        elif direction == 3:
            #good
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.image =  self.ship_image_list[5]

        elif direction == 4:
            #good
            self.rect.y += self.speed
            self.image =  self.ship_image_list[4]

        elif direction == 5:
            #good
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.image =  self.ship_image_list[3]

        elif direction == 6:
            #good
            self.rect.x -= self.speed
            self.image =  self.ship_image_list[2]

        elif direction == 7:
            #good
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.image =  self.ship_image_list[1]
        for b in self.bullet_list:
            b.update()


    def subtract_lives(self):
        if self.lives > 0:
            self.lives -= 1

    def get_lives(self):
        return self.lives

    def set_lives(self, lives_count):
        self.lives = lives_count

    def rotateImages(self):
        
        initial_rotation = 0
        for x in range (0, 8):
            temp_image = pygame.transform.rotate(self.image, initial_rotation)
            initial_rotation += 45
            self.ship_image_list.append(temp_image)

    def shoot(self, all_group):
        bullet = Bullet(self.rect.x,self.rect.y,self.direction)
        self.bullet_list.append(bullet)
        all_group.add(bullet)
        return all_group

