import pygame
pygame.init()

from constants import *
from player import Player
from asteroids import Asteroid, Shot, Particle
from asteroidfield import *
from gif import *


def main():
    
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock()
    dt = 0

    score = 0
    pygame.font.init()
    font = pygame.font.Font(None, 36)

    background = AnimatedBackground("assets/space.gif")

    particles = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    def create_explosion(x, y, color=(255, 255, 255), num_particles=20):
        for _ in range(num_particles):
            particle = Particle(x, y, color)
            particles.add(particle)
    
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
        particles.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                print("Game over!")
                import sys
                sys.exit()
        
        for asteroid in asteroids:
            for bullet in shots_group:
                if bullet.collision(asteroid) == True:
                    create_explosion(asteroid.position.x, asteroid.position.y)
                    bullet.kill()
                    asteroid.split()
                    if asteroid.radius == ASTEROID_MAX_RADIUS:
                        score += 25
                    elif asteroid.radius > ASTEROID_MIN_RADIUS and asteroid.radius < ASTEROID_MAX_RADIUS:
                        score += 50
                    elif asteroid.radius == ASTEROID_MIN_RADIUS:
                        score += 100

        screen.fill("black")
        background.update()
        background.render(screen)

        for object in drawable:
            object.draw(screen)
        shots_group.draw(screen)
        particles.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))

        screen.blit(score_text, (20, 20))
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()