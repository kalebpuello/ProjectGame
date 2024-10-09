import random
import pygame
class Fragmento:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = random.randint(2, radius // 2)
        self.color = color
        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-2, 2)

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def dibujar(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

