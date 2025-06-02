import pygame
from pygame.sprite import Sprite
import math
import time 

class EnemyBullet:
    def __init__(self, x, y, target_x, target_y):
        self.x, self.y = x, y
        self.speed = 5
        dx, dy = target_x - self.x, target_y - self.y
        distance = math.hypot(dx, dy)
        if distance == 0:
            self.dx, self.dy = 0, 0
        else:
            self.dx = dx / distance * self.speed
            self.dy = dy / distance * self.speed

    def  update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screeen):
        pygame.draw.circle(screen, (255,255, 0), (int(self.x), int(self.y)), 5)
    
    def is_off_screen(self, width, height):
        return (
            self.x < 0 or self.x > width or
            self.y < 0 or self.y > height 
        )

class EnemyShip:
    def __init__(self, x, y):
        self.x,  self.y = x, y
        self.speed = 3
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.bullets = []
        self.last_shot_time = 0
        self.shoot_cooldown = 1.0 #seconds

    def move_towards_player(self, player_x, player_y):
        dx, dy = player_x - self.x, player_y - self.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx, dy = dx / distance, dy / distace
            self.x += dx * self.speed
            self.y += dy * self.speed
            self.rect.topleft = (self.x, self.y)

    def shoot(self, player_x, player_y):
        """
        attempts to shoot a bullet toward player
        """
        now = time.time()
        if now - self.last_shot_time > self.shoot_cooldown:
            self.spawn_bullet(player_x, player_y)
            self.last_shot_time = now

    def spawn_bullet(self, player_x, player_y):
        """ 
        Bullet stars at center of the enemy ship
        """
        bullet_x = self.x + self.rect.wifth // 2
        bullet_y = self.y + self.rect.height // 2
        bullet = EnemyBullet(bullet_x, bullet_y, player_x, player_y)
        self.bullets.append(bullet)

    def update_bullets(self, screen, screen_width, screen_height):
        for bullet in self.bullets[:]:
            bullet.update()
            bullet.draw(screen)
            if bullet.is_off_screen(screen_width, screen_height):
                self.bullets.remove(bullet)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, player_x, player_y, screen, screen_width, screen_height):
        self.move_towards_player(player_x, player_y)
        self.try_shoot(player_x, player_y)
        self.update_bullets(screen, screen_width, screen_height)
        self.draw(screen)
