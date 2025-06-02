# Asteroid Game with AI-Driven Enemies: Architecture Overview

This document outlines the high-level architecture for an asteroid game in Python (using Pygame), extended with AI-driven enemies that can chase the player, shoot, and avoid obstacles.

---

## 1. **Core Modules & Their Responsibilities**

### a. **Game Engine (main loop)**
- Initializes game, loads resources, and controls the main loop.
- Handles user input, updates all game objects, and renders the screen.
- Manages game state (start, playing, game over) and score.

### b. **Player Ship**
- Handles player movement and shooting.
- Responds to user inputs.
- Detects collisions with asteroids, enemy bullets, and enemy ships.

### c. **Asteroids**
- Randomly spawned obstacles with varying sizes and directions.
- Moves autonomously across the screen.
- Detects collisions with player, enemies, and bullets.

### d. **Enemy Ships (AI)**
- Each enemy ship is an autonomous agent:
    - **Movement:** Tracks and chases the player.
    - **Shooting:** Fires projectiles toward the player at intervals.
    - **Obstacle Avoidance:** Changes trajectory to avoid asteroids.
- Can have multiple types (basic, fast, boss, etc.)

### e. **Projectiles/Bullets**
- Includes both player and enemy bullets.
- Move in straight lines once fired.
- Detect collisions with asteroids, enemy ships, and player ship.

### f. **Power-ups (optional, for expansion)**
- Provide temporary boosts (shields, faster fire, etc.)
- Dropped by destroyed asteroids or enemies.

---

## 2. **Class Relationships & Key Methods**

```
+-------------------+         +------------------+
|   Game Engine     |<------->|   Player Ship    |
+-------------------+         +------------------+
        |                             ^
        v                             |
+-------------------+         +------------------+
|    Asteroids      |<------->|   Enemy Ship(s)  |
+-------------------+         +------------------+
        ^                             ^
        |                             |
+-------------------+         +------------------+
|    Bullets        |<--------+------------------+
+-------------------+         | Power-Ups (opt.) |
                              +------------------+
```

### **Key Methods:**

**Game Engine**
- `run()`
- `spawn_asteroid()`
- `spawn_enemy()`
- `process_input()`
- `update_objects()`
- `draw_objects()`
- `check_collisions()`

**PlayerShip**
- `move(direction)`
- `shoot()`
- `draw(screen)`
- `check_collision(obj)`

**Asteroid**
- `update_position()`
- `draw(screen)`
- `check_collision(obj)`

**EnemyShip**
- `move_towards_player(player_pos, asteroids)`
- `try_shoot(player_pos)`
- `avoid_obstacles(asteroids)`
- `draw(screen)`
- `update_bullets(screen)`
- `check_collision(obj)`

**EnemyBullet**
- `update()`
- `draw(screen)`
- `check_collision(obj)`

---

## 3. **Game Loop Sequence**

1. **Input Handling**
    - Read keyboard/gamepad for player movement and shooting.

2. **Spawn Logic**
    - Spawn asteroids and enemy ships at intervals.

3. **Update Phase**
    - Move player, asteroids, enemy ships, and all bullets.
    - Enemy ships execute AI logic (chase, shoot, dodge).
    - Power-ups update (if any).

4. **Collision Detection**
    - Check all relevant collisions and handle consequences (damage, destruction, power-up pickup).

5. **Draw Phase**
    - Render all game objects to the screen.

6. **Game State Update**
    - Update score, check win/lose conditions, handle new levels.

---

## 4. **AI Enemy Architecture (Detail)**

- **Enemy Manager (optional):** Spawns and manages all enemy ships.
- **EnemyShip Instance:**
    - Maintains its own position, bullets, and cooldowns.
    - `move_towards_player()` for chasing.
    - `avoid_obstacles()` for steering clear of asteroids.
    - `try_shoot()` for firing at the player.
    - Manages its own bullets (`EnemyBullet` objects).

- **EnemyBullet:**
    - Moves toward target direction.
    - Notifies when off-screen or on collision.

---

## 5. **Extensibility Points**

- **New enemy types** (inherit from EnemyShip, override AI patterns).
- **Boss logic** (special movement and attack patterns).
- **Power-ups and Items** (extend pickup logic and spawn rules).
- **Sound and Visual Effects** (add explosion, shooting, and movement effects).

---

## 6. **File Structure Suggestion**

```
/asteroid_game/
    main.py               # Game loop and engine
    player.py             # Player ship class
    asteroid.py           # Asteroid class
    enemy.py              # EnemyShip & EnemyBullet classes
    bullet.py             # PlayerBullet (optional)
    powerup.py            # Power-ups (optional)
    utils.py              # Helper functions (optional)
    settings.py           # Game configuration constants
    assets/               # Sprites, sounds, etc.
    README.md
```

---

## 7. **Integration Tips**

- Keep update and draw methods separate for all objects.
- Loop through lists of asteroids, enemies, and bullets for updates/draws.
- Use Pygame's collision detection for rectangles/circles.
- Store all game objects in lists for easy update/removal.
- Consider an object manager for complex games.

---

## 8. **Next Steps**

- Implement and test each module/class independently.
- Integrate modules in the main game loop.
- Playtest and tweak AI behaviors and spawn rates.
- Expand with new features as desired!

---
