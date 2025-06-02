# AI-dr0id Enemies
 _"*AI ENEMIES INBOUND*"_

<!--![AsteroidAIdroid](https://github.com/user-attachments/assets/1b975e9b-ce23-46bb-b180-f59912da219a)

![asteroids_start_animation](https://github.com/user-attachments/assets/5bc89868-cc50-454e-9673-5bff3fd40b9d)-->


![asteroids_zoom_blur_animation (1)](https://github.com/user-attachments/assets/6eb4e346-e7bc-4fee-8675-8439351116c4)
> *Basic AI movement*

> *Enemy Droid Ship Atk logic*

> *State based AI dr0ids*
- AGRO
- DEFENSE
- RETREAT
> *Boss Fights*

> *Formation flying (dynamic)*
---


## 1. Pythonic Component Diagram

```plaintext
+---------------------+
|     Game Engine     |
+---------------------+
        |      |      \
        |      |       \ 
        v      v        v
+--------+ +--------+ +--------+
| Player | |Asteroid| | Enemy  |
|  Ship  | |  s     | | Ships  |
+--------+ +--------+ +--------+
     |         |         |
     |         |         |-------------------+
     |         |         |                   |
     v         v         v                   v
+-----------------------------------------------+
|              Projectiles/Bullets              |
+-----------------------------------------------+
        |
        v
+---------------------+
|   Collision System  |
+---------------------+
```

---

## 2. Module Breakdown

### a. **Game Engine (main.py)**
- Initializes and manages the game loop.
- Handles global state, event polling, object spawning, and orchestration.
- Calls update and draw methods for all game entities.

### b. **Player Ship (player.py)**
- Handles user input, movement, and firing bullets.
- Tracks health, score, and status.
- Detects collisions with asteroids, enemy bullets, and enemy ships.

### c. **Asteroids (asteroid.py)**
- Randomly generated with various sizes, speeds, and trajectories.
- Moves autonomously and wraps around screen edges.
- Detects collisions with player, enemy ships, and projectiles.

### d. **Enemy Ships (enemy.py)**
- Autonomous AI agents:
    - Move toward player using vector math.
    - Avoid asteroids (basic obstacle avoidance).
    - Fire projectiles with cooldown logic.
    - Can be extended to multiple types (e.g. boss, fast, swarm).
- Each manages its own bullets/projectiles.

### e. **Projectiles (bullet.py)**
- Includes both player and enemy bullets.
- Moves in a specified direction with constant speed.
- Tracks its own lifetime and collision status.

### f. **Collision System (utils.py / inside main.py)**
- Checks overlap between all relevant game entities:
    - Player vs. asteroid, enemy, or bullet.
    - Enemy vs. asteroid or player bullet.
    - Bullet vs. asteroid or ship.
- Handles resulting actions (damage, destruction, scoring).

### g. **Power-ups (powerup.py, optional)**
- Spawned on certain events (e.g. asteroid or enemy destruction).
- Provides temporary boosts (shield, rapid fire, etc.).

### h. **Assets (assets/)**
- Contains graphics, sound effects, and fonts.

---

## 3. Suggested File Structure

```
/asteroid_game/
    main.py            # Game loop and orchestration
    player.py          # PlayerShip class
    asteroid.py        # Asteroid class
    enemy.py           # EnemyShip & EnemyBullet classes
    bullet.py          # PlayerBullet class
    powerup.py         # (Optional) PowerUp class
    utils.py           # Helper/collision functions
    settings.py        # Game constants and configs
    assets/            # Images, sounds, fonts
    README.md
    ARCHITECTURE_BLUEPRINT.md
```

---

## 8. Notes

- Use Pygame’s rect/circle collision methods for simplicity.
- Store all dynamic entities (asteroids, enemies, bullets) in lists for easy update/removal.
- Keep logic for each entity self-contained for maintainability.
- Tune AI parameters (speed, cooldown, avoidance strength) for fun gameplay.

---

