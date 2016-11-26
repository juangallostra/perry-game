# perry_game
Game about eating smaller platypus and avoid being eaten by bigger ones.

Requirements:
- Python 2.7
- Pygame

All project files (code and images) should be located in the same folder. Run init.py to start the game.

A little explanation about what is inside each file:
- init.py: Main loop of the game. It renders the background, the player character and the enemies. It also checks for collisions between player and enemies and reads player input.
- perry.py: File that holds the class of the player's character. It just contains the class, which inherits from pygame.sprite.Sprite, with its attributes and methods.
- enemy.py: File that holds the class of the enemies. It just contains the class, which inherits from pygame.sprite.Sprite, with its attributes, methods, and enemy AI.
- control.py: Contains several functions that are called in the main loop. It mainly improves readability 
