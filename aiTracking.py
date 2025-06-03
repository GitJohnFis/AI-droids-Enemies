import pygame
import math
# import all the basic tracking AI dependencies

class EnemyShip:
  def __init__(self, x, y):
    self.x, self.y = x, y
    self.speed = 3
    self.agro_speed = 6 #increased or 2x speed for AGRO mode
    self.color = (255, 0, 0) #red AI-enemy 
    self.rect = pygame.Rect(self.x, self.y, 40, 40)
    self.state = "normal" # AI state can be Normal, Defensive, or Aggressive
    self.agro_timer = 0
    self.base_speed = self.speed #base speed for normal state

  def move_towards_player(self, player_x, player_y):
    dx, dy = player_x - self.x, player_y - self.y
    distance = math.sqrt(dx**2 + dy**2)

    if distance > 1e-6: #!= 0:
      """ If the distance between the enemy and the player is very small (but not zero),
       dividing by it can cause jittery movement due to floating-point precision issues.
      To prevent erratic AI behavior, use a small epsilon value to avoid division by 
       extremely small numbers.
    """
      dx, dy = dx/distance, dy/distance #normal direction for player
      speed = self.agro_speed if self.state == "agro" else self.base_speed #implement the AGRO logic
      self.x += dx * self.speed
      self.y += dy * self.speed
      self.rect.topleft = (self.x, self.y)

def draw(self, screen):
  pygame.draw.rect(screen, self.color, self.rect)

def set_agro(self, duration=300): #duration in frames (e.g., 5 seconds at 60fps)
    self.state = 'agro'
    self.agro_timer = duration

def update(self, player_x, player_y):
    """ 
    AGRO timer logic when it runs
    """
    if self.state == "agro":
        if hasattr(self, "agro_timer") and self.agro_timer > 0:
            self.agro_timer -= 1
    else:
        self.state = "normal"
    self.move_towards_player(player_x, player_y)


#Add this new code with three new states(retreat, AGRO, Defense)
# import pygame
# import math
# from state import EnemyState

# class EnemyShip:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#         self.state = EnemyState.RETREAT
#         self.retreat_speed = 2
#         self.defense_speed = 3
#         self.agro_speed = 6
#         self.color = (255, 0, 0)
#         self.rect = pygame.Rect(self.x, self.y, 40, 40)
#         self.agro_timer = 0

#     def set_state(self, new_state, duration=None):
#         self.state = new_state
#         if new_state == EnemyState.AGRO and duration:
#             self.agro_timer = duration

#     def update(self, player_x, player_y):
#         # AGRO timer logic
#         if self.state == EnemyState.AGRO and self.agro_timer > 0:
#             self.agro_timer -= 1
#             if self.agro_timer == 0:
#                 self.state = EnemyState.DEFENSE

#         self.move_by_state(player_x, player_y)

#     def move_by_state(self, player_x, player_y):
#         dx, dy = player_x - self.x, player_y - self.y
#         distance = math.hypot(dx, dy)
#         if distance > 1e-6:
#             dx, dy = dx / distance, dy / distance
#             if self.state == EnemyState.RETREAT:
#                 # Move away from player
#                 speed = self.retreat_speed
#                 self.x -= dx * speed
#                 self.y -= dy * speed
#             elif self.state == EnemyState.DEFENSE:
#                 # Move perpendicular (evasive action)
#                 speed = self.defense_speed
#                 self.x += -dy * speed
#                 self.y += dx * speed
#             elif self.state == EnemyState.AGRO:
#                 # Move aggressively toward player
#                 speed = self.agro_speed
#                 self.x += dx * speed
#                 self.y += dy * speed
#             self.rect.topleft = (self.x, self.y)

#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, self.rect)


