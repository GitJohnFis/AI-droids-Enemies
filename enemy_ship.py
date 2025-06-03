import pygame
import math

class EnemyShip:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.speed = 3
        self.color = (255, 0, 0) # red AI-enemy
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def move_towards_player(self, player_x, player_y):
        dx, dy = player_x - self.x, player_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance > 1e-6:
            dx, dy = dx/distance, dy/distance
            self.x += dx * self.speed
            self.y += dy * self.speed
            self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)