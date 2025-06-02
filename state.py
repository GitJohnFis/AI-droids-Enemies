
"""
Defines possible states for enemy ships in the game.
"""

from enum import Enum, auto

class EnemyState(Enum):
    RETREAT = auto()  # Retreat: tries to escape or avoid the player, lowest aggression
    DEFENSE = auto()  # Defensive: evades or uses cover, moderate aggression
    AGRO = auto()     # Aggressive: relentless pursuit, fastest, hard mode

    def describe(self):
        if self is EnemyState.RETREAT:
            return "Retreat: avoids the player, tries to escape or keep distance."
        elif self is EnemyState.DEFENSE:
            return "Defense: evades, uses cover, attacks cautiously."
        elif self is EnemyState.AGRO:
            return "AGRO: relentless pursuit, high speed, most aggressive mode."
        else:
            return "Unknown state."

# Example usage
if __name__ == "__main__":
    for state in EnemyState:
        print(f"{state.name}: {state.describe()}")
