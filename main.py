# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=PLAYER_RADIUS)
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        dt = game_clock.tick(60) / 1000
        player.update(dt)
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()

