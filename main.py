import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

# Our main game loop
    while True:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player) == True:
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.colliding(asteroid) == True:
                    asteroid.split()
        
        screen.fill(color=000000)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()