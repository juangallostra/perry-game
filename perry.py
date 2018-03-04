
import pygame

# Class for the main player 

class Perry(pygame.sprite.Sprite):
    '''
    This class is the player's class which inherits from pygame.sprite.Sprite class
    ---ATTRIBUTES---

    ---METHODS---
    '''

    # Class initialization
    def __init__(self, perry_image, initial_x, initial_y, speed): 
        pygame.sprite.Sprite.__init__(self) # Inherit from pygame.Sprite class
        self.image = pygame.image.load(perry_image).convert() # Load player's image
        self.image = pygame.transform.scale(self.image,(32,46)) # Starting  player size
        self.image.set_colorkey((255,255,255)) # Turns white in the image to transparent
        self.size = self.image.get_size() # Get size of the player
        # Player's x and y coordinates
        self.x = initial_x 
        self.y = initial_y
        # Get sprite rectangle
        self.rect = self.image.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        self.speed = speed

    # Method for increasing player's size when eating an enemy
    def grow(self,enemy): 
        # Only if future size < max size
        if self.size[1]+int(enemy.size[1]/10) < 550:
           # Reload image and scale it and create new rectangle
    	   self.image = pygame.image.load('perry.png').convert()
           self.image = pygame.transform.scale(self.image,(self.size[0]+int(enemy.size[0]/10),self.size[1]+int(enemy.size[1]/10))) 
    	   self.image.set_colorkey((255,255,255))
           self.rect = self.image.get_rect()
    	   self.rect.x = self.x
    	   self.rect.y = self.y
    	   self.size = self.image.get_size()

    # Methods for moving the player. Speed is 5 pixels/tic and both sprite and rectangle are moved
    def moveup(self):
    	if self.y-self.speed > 0:		
    		self.y -= self.speed
    		self.rect.y -= self.speed

    def movedown(self):
    	if self.y+self.speed+self.size[1] < 640:
    		self.y += self.speed
    		self.rect.y += self.speed

    def moveleft(self):
    	if self.x-self.speed > 0:
    		self.x -= self.speed
    		self.rect.x -= self.speed

    def moveright(self):
    	if self.x+self.speed+self.size[0] < 1152:
    		self.x += self.speed
    		self.rect.x += self.speed

    def flip(self):
         self.image = pygame.transform.flip(self.image, True, False)
