# TODO: redefine magic numbers as constants

import pygame
import random

# Class for the main player 

class Enemy(pygame.sprite.Sprite):
    '''
    This class is the enemy class which inherits from pygame.sprite.Sprite class
    '''
    # Class initialization
    def __init__(self, enemy_img, size, game_window_x, game_window_y): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(enemy_img).convert() # Load enemy image
        self.image = pygame.transform.scale(self.image,size) # Enemy size
        self.image.set_colorkey((255,255,255)) # Turns white in the image to transparent
        self.rect = self.image.get_rect() # Get position of the enemy
        self.size = self.image.get_size() # Get size of the enemy
        self.direction = [random.random()*random.choice([1,-1]),random.random()*random.choice([1,-1])] #movement direction
        # Starting position
        self.x = random.random()*1000
        self.y = random.random()*640
        # Game window size
        self.game_window_x = game_window_x
        self.game_window_y = game_window_y
        # Movement target
        self.target_x = int(random.random()*self.game_window_x)-self.size[0]
        self.target_y = int(random.random()*self.game_window_x)-self.size[1]
        # Defining speed
        self.speed = random.choice([1,2,5,7])
        # Get sprite rectangle
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.counter = random.randint(0,120)
        # Store directions to flip sprites accordingly
        self.last_dir = 'RIGHT'
        self.last_dir_1 = 'RIGHT'

    # Redefine target, speed and direction
    def target_dir_speed(self):
        # Restart counter
        self.counter = random.randint(0,120)
        # Redefine target
        self.target_x = random.randrange(0,self.game_window_x-self.size[0])
        self.target_y = random.randrange(0,self.game_window_y-self.size[1])
        # Set speed
        self.speed = random.choice([1,2])
        # Set direction
        m = float(self.target_y-self.y)/float(self.target_x-self.x)
        while m>abs(1.73):
            self.target_x = random.randrange(0,self.game_window_x-self.size[0])
            self.target_y = random.randrange(0,self.game_window_y-self.size[1])
            m = float(self.target_y-self.y)/float(self.target_x-self.x)

        self.direction = [float(self.target_x-self.x)/abs(self.target_x-self.x),(float(self.target_y-self.y)/abs(self.target_y-self.y))*m]

    # Method for moving the enemy
    def move(self):
        # Check to see if enemy is on target and, if True, redefine movement parametres
        if self.x in range(self.target_x-15,self.target_x+15) and self.y in range(self.target_y-15,self.target_y+15) or self.counter==0:
            Enemy.target_dir_speed(self)
        # Else move
        else:
            if 0<self.x+self.direction[0]*self.speed<1152-self.size[0]:
                self.x+=self.direction[0]*self.speed
                self.rect.x = self.x
                
                # Update facing sprite direction
                self.last_dir = self.last_dir_1
                if self.direction[0]*self.speed > 0:
                    self.last_dir_1 = 'RIGHT'
                else:
                    self.last_dir_1 = 'LEFT'
                if self.last_dir != self.last_dir_1:
                    self.image = pygame.transform.flip(self.image, True, False)
            else:
                self.direction[0]=-1*self.direction[0]

            if 0<self.y+self.direction[1]*self.speed<640-self.size[1]:
                self.y+=self.direction[1]*self.speed
                self.rect.y = self.y
            else:
                self.direction[1]=-1*self.direction[1]
            self.counter-=1

        

    # Method for growing enemy
    def grow(self,perry,flag): 
        y=random.choice([0,1])
        # Only if future size < max size and flag==collision==True and choice==1
        if self.size[1]+int(perry.size[1]/10)<550 and flag==True and y==1:
           # Reload image and scale it and create new rectangle
           self.image=pygame.image.load('perry.png').convert()
           self.image=pygame.transform.scale(self.image,(self.size[0]+int(perry.size[0]/10),self.size[1]+int(perry.size[1]/10))) 
           self.image.set_colorkey((255,255,255))
           self.rect=self.image.get_rect()
           self.rect.x=self.x
           self.rect.y=self.y
           self.size=self.image.get_size()

    def flip(self):
             self.image = pygame.transform.flip(self.image, True, False)
