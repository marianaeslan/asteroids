# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        # Rever esse bloco de codigo
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                exit() 

        for obj in drawable:
            obj.draw(screen)

        dt = game_clock.tick(60) / 1000
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()

