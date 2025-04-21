import pygame
pygame.init()

from constants import *
from player import Player
from asteroids import Asteroid, Shot
from asteroidfield import *


def main():
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x=650, y=360)
    player.shots_group = shots_group

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.container = (shots_group, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        shots_group.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                print("Game over!")
                import sys
                sys.exit()
        
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)
        shots_group.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()