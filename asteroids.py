import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
            
        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_1.velocity = new_velocity_1
        new_asteroid_2.velocity = new_velocity_2

        
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            5
        )

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt



class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.velocity = pygame.math.Vector2(0, 0)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)



class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(255, 255, 255)):
        super().__init__()

        self.image = pygame.Surface((4, 4), pygame.SRCALPHA)

        pygame.draw.circle(self.image, color, (2, 2), 2)

        self.rect = self.image.get_rect(center=(x, y))
        
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.lifetime = random.randint(30, 60)

    def update(self, *args):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()