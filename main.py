import pygame # import the pygame library
from player import *
from constants import * # import everything from constants.py

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    player.rotate(dt)

# Our main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        player.update(dt)
        
        screen.fill(color=000000)
        player.draw(screen)
        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()