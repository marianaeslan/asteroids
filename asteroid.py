import pygame
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, position, radius):
       self.position = position
       self.radius = radius
    
    def draw(self, surface):
        pygame.draw.circle(surface, "green", self.position, self.radius, 2)