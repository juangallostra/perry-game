import pygame
import perry
import enemy
import random


## CONSTANTS
TILE_SIZE = 64 

## HELPER FUNCTIONS


# Create background: Fills the background surface with tiles (64x64) of grass and blits it to the pygame display window
def draw_background(BACK, tile_img, size):
    background = pygame.Surface(size)
    TILE = pygame.image.load(tile_img).convert()
    x = 0
    y = 0
    while x < size[0]:
        while y < size[1]:
            background.blit(TILE,(x,y))	# Tile size is 64x64
            y += TILE_SIZE				
        y = 0
        x += TILE_SIZE
    BACK.blit(background,(0,0))


# Draws character into screen
def draw_character(BACK,Player): 
    BACK.blit(Player.image,(Player.x,Player.y))

# Draws "game over" screen
def draw_loser(BACK,photo,size):
    photo = pygame.image.load(photo)
    photo = pygame.transform.scale(photo,size)
    BACK.blit(photo,(0,0))
    

# Checks wether player eats enemey or enemy eats player
def eating(Perry,enemy):
	if Perry.size >= enemy.size: #size check
		return True
	else:
		return False
