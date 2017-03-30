# perry_game
Simple game about eating smaller platypus and avoid being eaten by bigger ones.

## Requirements:
- Python 2.7
- Pygame
- All project files (code and images) should be located in the same folder. Run main.py to start the game.

## Files
A little explanation about what is inside each file:
- ```main.py```: Main loop of the game. It renders the background, the player character and the enemies. It also checks for collisions between player and enemies and reads player input.
- ```perry.py```: File that holds the class of the player's character. It just contains the class, which inherits from pygame.sprite.Sprite, with its attributes and methods.
- ```enemy.py```: File that holds the class of the enemies. It just contains the class, which inherits from pygame.sprite.Sprite, with its attributes, methods, and enemy AI.
- ```helper.py```: Contains several functions that are called in the main loop. It mainly improves readability

## TODO
- *fix bug* enemy spawns. From time to time the number of enemies that appear goes wild.
- *fix bug* enemy speed. When the direction of movement of the enemies is close to +-90º the enemy displacement along the y-axis is huge.
- *Improve* the enemy movement and the ratio of appearance and total number of enemies in the screen.
 
