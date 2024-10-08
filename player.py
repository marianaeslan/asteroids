import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.lives = 3

        # Load and scale the image for the player (spaceship image)
        self.original_image = pygame.image.load("spaceship.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (PLAYER_RADIUS * 4, PLAYER_RADIUS * 4))
        self.image = self.original_image  # This will hold the rotated image

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
       # Rotate the image based on the player's rotation
        rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)

        # Get the rect for positioning and center it at the player's position
        rect = rotated_image.get_rect(center=(self.position.x, self.position.y))

        # Blit the rotated image to the screen
        screen.blit(rotated_image, rect.topleft)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(dt * -1)
        if self.shoot_timer <= 0:  # Can only shoot if the timer is 0 or less
            if keys[pygame.K_SPACE]:
                self.shoot()
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset timer
        else:
            self.shoot_timer -= dt  # Decrease the cooldown timer
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt