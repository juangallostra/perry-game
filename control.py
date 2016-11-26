import pygame
import perry
import enemy
import random


##CONTROL FUNCTIONS


#create background: Fills the background surface with tiles (64x64) of grass and blits it to the pygame display window
def draw_background(BACK,a,size):
    background=pygame.Surface(size)
    TILE=pygame.image.load(a).convert()
    x=0
    y=0
    while x<size[0]:
        while y<size[1]:
            background.blit(TILE,(x,y))
            y+=64
        y=0
        x+=64
    BACK.blit(background,(0,0))


#draws character into screen
def draw_character(BACK,Player): 
    BACK.blit(Player.image,(Player.x,Player.y))

#draws game over screen
def draw_loser(BACK,photo,size):
    photo=pygame.image.load(photo)
    photo=pygame.transform.scale(photo,size)
    BACK.blit(photo,(0,0))
    

#function for checking wether player eats enemey or enemy eats player
def eating(Perry,enemy):

	if Perry.size>=enemy.size: #size check
		return True
	else:
		return False
