flowchart TD
    subgraph Engine["Game Engine (main.py)"]
        direction TB
        Input["Input Handler"]
        Spawn["Spawner"]
        Updater["Update Manager"]
        Drawer["Draw Manager"]
        State["Game State Manager"]
        EngineCore["Core Loop"]
        EngineCore --> Input
        EngineCore --> Spawn
        EngineCore --> Updater
        EngineCore --> Drawer
        EngineCore --> State
    end

    subgraph Assets["Assets & Resources (assets/)"]
        Sprites["Sprites"]
        Sounds["Sound Effects"]
        Fonts["Fonts"]
        Configs["Config Files"]
    end

    subgraph Entities["Game Entities"]
        Player["Player Ship (player.py)"]
        Asteroids["Asteroids (asteroid.py)"]
        EnemyManager["Enemy Manager (enemy_manager.py)"]
        EnemyShips["Enemy Ships (enemy.py)"]
        Bullets["Projectiles/Bullets (bullet.py)"]
        PowerUps["Power-Ups (powerup.py)"]
    end

    subgraph AI["AI & Behavior"]
        EnemyAI["Enemy AI (enemy_ai.py)"]
        FormationAI["Formation AI (formation_ai.py)"]
        BossLogic["Boss Logic (boss_ai.py)"]
    end

    subgraph Systems["Systems"]
        Collision["Collision System (collision.py)"]
        Physics["Physics Engine (physics.py)"]
        Score["Score & Progress (score.py)"]
        Level["Level Manager (level.py)"]
        UI["UI/HUD (ui.py)"]
        Save["Save/Load (save.py)"]
    end

    %% Connections from Engine to entities and systems
    EngineCore --> Entities
    EngineCore --> Systems
    EngineCore --> Assets

    %% Player and Enemy interaction
    Player <--> Bullets
    Player <--> Asteroids
    Player <--> EnemyShips
    Player <--> PowerUps
    Player -->|shoots| Bullets

    EnemyManager --> EnemyShips
    EnemyShips -->|uses| EnemyAI
    EnemyShips -->|shoots| Bullets
    EnemyShips -->|can become| BossLogic

    EnemyShips <--> Asteroids
    EnemyShips <--> Bullets
    EnemyShips -->|formation| FormationAI

    Bullets <--> Asteroids
    Bullets <--> EnemyShips
    Bullets <--> Player

    PowerUps --> Player

    %% Systems interaction
    Entities --> Collision
    Entities --> Physics
    Collision --> State
    Collision --> Score
    Collision --> Level

    Level --> Spawn
    Level --> Entities
    Level --> State

    UI --> EngineCore
    UI --> Score
    UI --> State

    Save --> State
    Save --> Score

    %% Assets dependencies
    Assets --> Player
    Assets --> Asteroids
    Assets --> EnemyShips
    Assets --> Bullets
    Assets --> PowerUps
    Assets --> UI

    %% Robustness: Extensibility & Managers
    subgraph Extensibility["Extensibility Points"]
        Mods["Mod Support"]
        Networking["Multiplayer/Networking"]
        Analytics["Analytics/Telemetry"]
        Debugger["Debug Tools"]
    end

    EngineCore --> Extensibility
    Entities --> Extensibility
    Systems --> Extensibility
