import pygame
from circleshape import CircleShape
from constants import *
from asteroids import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
        )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE] and hasattr(self, 'shots_group'):
            self.shoot()


    def shoot(self):
        direction = pygame.math.Vector2(0, 1)
        rotated_direction = direction.rotate(self.rotation)
        velocity = rotated_direction * PLAYER_SHOOT_SPEED
        
        shot_position = pygame.math.Vector2(self.position)
        
        new_shot = Shot(shot_position.x, self.position.y)
        new_shot.velocity = velocity
        
        self.shots_group.add(new_shot)







    
    if __name__ == "__main__":
        print("Player class defined")
