import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

class Shot(CircleShape, pygame.sprite.Sprite):  # Inherit from both CircleShape and Sprite
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        
        # Create the image for the sprite
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        
        # Set the rect for positioning
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.velocity = pygame.math.Vector2(0, 0)
    
    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)