
import pygame

# Class for the main player 

class Perry(pygame.sprite.Sprite):
    '''
    This class is the player's class which inherits from pygame.sprite.Sprite class
    ---ATTRIBUTES---

    ---METHODS---
    '''

    # Class initialization
    def __init__(self,a): 
        pygame.sprite.Sprite.__init__(self) # Inherit from pygame.Sprite class
        self.image=pygame.image.load(a).convert() # Load player's image
        self.image=pygame.transform.scale(self.image,(32,46)) # Starting  player size
        self.image.set_colorkey((255,255,255)) # Turns white in the image to transparent
        self.size=self.image.get_size() # Get size of the player
        # Player's x and y coordinates
        self.x=500 
        self.y=500
        # Get sprite rectangle
        self.rect=self.image.get_rect() 
        self.rect.x=self.x
        self.rect.y=self.y

    # Method for increasing player's size when eating an enemy
    def grow(self,enemy): 
        # Only if future size < max size
        if self.size[1]+int(enemy.size[1]/10)<550:
           # Reload image and scale it and create new rectangle
    	   self.image=pygame.image.load('perry.png').convert()
           self.image=pygame.transform.scale(self.image,(self.size[0]+int(enemy.size[0]/10),self.size[1]+int(enemy.size[1]/10))) 
    	   self.image.set_colorkey((255,255,255))
           self.rect=self.image.get_rect()
    	   self.rect.x=self.x
    	   self.rect.y=self.y
    	   self.size=self.image.get_size()

    # Methods for moving the player. Speed is 5 pixels/tic and both sprite and rectangle are moved
    def moveup(self):
    	if self.y-5>0:		
    		self.y-=5
    		self.rect.y-=5

    def movedown(self):
    	if self.y+5+self.size[1]<640:
    		self.y+=5
    		self.rect.y+=5

    def moveleft(self):
    	if self.x-5>0:
    		self.x-=5
    		self.rect.x-=5


    def moveright(self):
    	if self.x+5+self.size[0]<1152:
    		self.x+=5
    		self.rect.x+=5

    def flip(self):
         self.image = pygame.transform.flip(self.image, True, False)
        
