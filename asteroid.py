import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        if self.radius / 2 < ASTEROID_MIN_RADIUS:
            return []
        else:
            random_angle = random.uniform(20,50)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = self.velocity.rotate(random_angle) * 1.2 
            a2.velocity = self.velocity.rotate(-random_angle) * 1.2
            return [a1, a2]
    