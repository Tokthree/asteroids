import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        split_vector_a = self.velocity.rotate(random_angle)
        split_vector_b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_a.velocity = split_vector_a * 1.2
        split_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_b.velocity = split_vector_b * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt