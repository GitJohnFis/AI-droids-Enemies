```mermaid
flowchart TD
    GameEngine["Game Engine (main.py)"]
    PlayerShip["Player Ship (player.py)"]
    Asteroids["Asteroids (asteroid.py)"]
    EnemyShips["Enemy Ships (enemy.py)"]
    Bullets["Projectiles/Bullets (bullet.py)"]
    Collision["Collision System (utils.py)"]
    PowerUps["Power-Ups (powerup.py)"]
    Assets["Assets (assets/)"]

    GameEngine --> PlayerShip
    GameEngine --> Asteroids
    GameEngine --> EnemyShips
    GameEngine --> PowerUps
    GameEngine --> Assets

    PlayerShip -->|fires| Bullets
    EnemyShips -->|fires| Bullets
    PlayerShip -->|collides| Collision
    EnemyShips -->|collides| Collision
    Asteroids -->|collides| Collision
    Bullets -->|collides| Collision
    PowerUps -->|collected by| PlayerShip

    EnemyShips -->|avoids| Asteroids
    EnemyShips -->|chases| PlayerShip

    GameEngine --> Collision
    GameEngine --> Bullets
