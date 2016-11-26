
import pygame
import perry
import helper
import enemy
import random


##------------ GAME ---------------

## INITIALIZATION

running = True
eaten   = False
col     = False
smaller = False

pygame.init()
NE_MAX=5
BACK=pygame.display.set_mode((1152,640))
PERRY=perry.Perry('perry.png')
clock=pygame.time.Clock()
enemies=pygame.sprite.Group()

last_pressed_1_perry = 'RIGHT'
last_pressed_2_perry = 'RIGHT'

## MAIN_LOOP

while running:
    
    clock.tick(60) # Limit to a max of 60fps

    # Make sure we have the assigned number of enemies
    while len(enemies) < int((NE_MAX*50)/PERRY.size[0]):
        ratio=float(random.choice([-20,-10,0,20,30]))/100
        size=(PERRY.size[0]+int(ratio*PERRY.size[0]),PERRY.size[1]+int(ratio*PERRY.size[1]))
        enemies.add(enemy.Enemy('perry.png',size))

    # Grow alive enemies and check for smaller enemies
    for enem in enemies:
        enem.grow(PERRY,col)
        if enem.size<=PERRY.size:
            smaller=True
        else:
            smaller=False
    # In case there is no smaller enemy, create one
    if smaller==False:
        size=(PERRY.size[0]-PERRY.size[0]/10,PERRY.size[1]-PERRY.size[1]/10)
        enemies.add(enemy.Enemy('perry.png',size))
        smaller=True

    # Check for events and act in accordance
    for event in pygame.event.get():

        # Exiting the game
        if event.type == pygame.QUIT:
            running=False

    
    # Moving the player
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        PERRY.moveleft()
        last_pressed_1_perry = last_pressed_2_perry
        last_pressed_2_perry = 'LEFT'
    if keys[pygame.K_RIGHT]:
        PERRY.moveright()
        last_pressed_1_perry = last_pressed_2_perry
        last_pressed_2_perry = 'RIGHT'
    if keys[pygame.K_UP]:
        PERRY.moveup()
    if keys[pygame.K_DOWN]:
        PERRY.movedown()

    # Flip character sprite if necessary
    if last_pressed_1_perry != last_pressed_2_perry:
        PERRY.flip()

    # Check for collisions and, if there is any, check who eats who
    col_list=pygame.sprite.spritecollide(PERRY,enemies,True)
    col=False
    for enem in col_list:
        if helper.eating(PERRY,enem)==True:
            PERRY.grow(enem)
            col=True
        else:
            eaten=True
            enemies.add(enem)
            

    # Screen update, which contains two branches: Keep playing or losing the game.
    # Eaten is the flag to control the conditional and program flow.

    # Game over (case eaten).
    if eaten==True:
        helper.draw_loser(BACK,'loser_1.png',(1152,640))
        pygame.display.flip()
        while eaten==True:
            for event in pygame.event.get(): # Check for events and act in accordance
                # Restarting the game
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_SPACE:
                        eaten = False
                        enemies = pygame.sprite.Group()
                        PERRY=perry.Perry('perry.png')
                        last_pressed_1_perry = 'RIGHT'
                        last_pressed_2_perry = 'RIGHT'
                        
                # Exiting the game
                elif event.type == pygame.QUIT:
                    running=False
    # Keep playing (case no collision or enemy eaten)
    else:
        helper.draw_background(BACK,'grass4.png',(1152,640))
        helper.draw_character(BACK,PERRY)
        for enem in enemies:
            enem.move()
            helper.draw_character(BACK,enem)
        pygame.display.flip()
    

