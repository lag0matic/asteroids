from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField 



import pygame

clock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable,)

def main():
    dt = 0
    pygame.init()
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    player = Player( x, y )
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                return
        
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0
    


if __name__ == "__main__":
    main()
