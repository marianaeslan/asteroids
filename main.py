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
    game_over = False  # To track if the game is over
    game_over_timer = 0  # To control how long the "Game Over" screen is displayed


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

        if not game_over:
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
                        game_over = True  # Trigger game over state
                        game_over_timer = pygame.time.get_ticks()  # Start timer
                    asteroid.kill()  # Destroy the asteroid
                    break

            # Check for bullet collisions with asteroids
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

            # Display score and lives
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))  # Top-left corner for score
            lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
            screen.blit(lives_text, (SCREEN_WIDTH - 120, 10))  # Top-right corner for lives
        else:
            # Game over screen
            screen.fill("black")  # Fill the screen with black

            # Display "Game Over" and score
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
            final_score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
            screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

            # Check if 3 seconds have passed
            if pygame.time.get_ticks() - game_over_timer > 3000:
                running = False  # Exit the game after 3 seconds
         

        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()

