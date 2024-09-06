import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    score = 0  # New score variable

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    # Groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers for Player, Asteroid, and Shot
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    font = pygame.font.Font(None, 36)  # Load a font for displaying the score
    dt = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = game_clock.tick(60) / 1000

        # Update all objects in the 'updatable' group
        for obj in updatable:
            obj.update(dt)

        # Clear screen
        screen.fill("black")

        # Check collision between player and asteroid
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                player.lives -= 1  # Decrease life by 1
                if player.lives <= 0:
                    game_over_text = font.render("Game Over", True, (255, 0, 0))  # Red color
                    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                    screen.blit(game_over_text, text_rect)  # Draw the text
                    pygame.display.flip()  # Update the display
                    pygame.time.wait(2000)  # Wait for 2 seconds
                    running = False
                    exit()
                asteroid.kill()  # Destroy the asteroid
                break

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    asteroid.kill()
                    score += 100

        # Draw all objects in the 'drawable' group
        for obj in drawable:
            obj.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
        screen.blit(score_text, (10, 10))  # Display at the top-left corner

        # Draw the lives on the screen
        lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
        lives_rect = lives_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))  # Position lives text at top-right corner
        screen.blit(lives_text, lives_rect)         

        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()

