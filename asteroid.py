import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Load and scale the asteroid image
        self.image = pygame.image.load("asteroid.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))  # Scale based on radius
        
        # Create a rotated version of the image to match the asteroid's movement
        self.angle = random.uniform(0, 360)
        self.image = pygame.transform.rotate(self.image, self.angle)
        
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.rect.center = self.position

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        #Kill the current asteroid
        self.kill()
        # Check if the asteroid is too small to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)

        #calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two velocity vectors by rotating the original velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Scale up speed by 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Create two new asteroids with the smaller radius
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Assign the new velocity vectors to the new asteroids
        new_asteroid1.velocity = velocity1
        new_asteroid2.velocity = velocity2
