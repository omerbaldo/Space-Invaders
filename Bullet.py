import pygame

class Bullet(pygame.sprite.Sprite): # inherits from the pygame sprite class

    def __init__(self,x,y,direction):#initialization, takes itsself as an arguement
        super(Bullet,self).__init__() # initializes parent class
    
        self.image = pygame.image.load("images/lazer.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x+130, y)) # init x and y
        self.direction = direction

        self.initial_rotation = 0
        self.bullet_image_list = []
        self.rotateImages()
        self.speed = 50
        #rotateImages() # get eight images for rotation 

    def update(self):
        #print self.direction

        if self.direction == 0:
            #print "update"
            self.rect.y -= self.speed
            self.image =  self.bullet_image_list[0]
            # good

        elif self.direction == 1:
            #good
            #print "update"
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.image =  self.bullet_image_list[7]

        elif self.direction == 2:
            #good
            #print "update"
            self.rect.x += self.speed
            self.image =  self.bullet_image_list[6]

        elif self.direction == 3:
            #good
            #print "update"
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.image =  self.bullet_image_list[5]

        elif self.direction == 4:
            #good
            #print "update"
            self.rect.y += self.speed
            self.image =  self.bullet_image_list[4]

        elif self.direction == 5:
            #good
            #print "update"
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.image =  self.bullet_image_list[3]

        elif self.direction == 6:
            #good
            #print "update"
            self.rect.x -= self.speed
            self.image =  self.bullet_image_list[2]

        elif self.direction == 7:
            #good
            #print "update"
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.image =  self.bullet_image_list[1]

    def rotateImages(self):
    
        initial_rotation = 0
        for x in range (0, 8):
            temp_image = pygame.transform.rotate(self.image, initial_rotation)
            initial_rotation += 45
            self.bullet_image_list.append(temp_image)