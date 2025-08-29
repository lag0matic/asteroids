from constants import *
from player import Player
from circleshape import CircleShape

import pygame

clock = pygame.time.Clock()
def main():
    dt = 0
    pygame.init()
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    player = Player( x, y )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0
    


if __name__ == "__main__":
    main()
