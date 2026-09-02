"""
PLAYER CLASS
============
Extends Character class with player-specific mechanics. The player is controlled by the user
and has progression systems like leveling, experience, and potentially inventory.

REQUIREMENTS:
1. Inherits from Character:
	- Gets all base character methods and attributes
	- Call super().__init__() in Player's __init__

2. Player-Specific Attributes:
	- level (int) - starts at 1
	- experience (int) - starts at 0
	- experience_to_next_level (int) - threshold for leveling (ex: 100 * level)
	- inventory (list or dict) - optional, for items/equipment
	- mana or special_points (int) - optional, for abilities beyond basic attack

3. Player-Specific Methods:
	- gain_experience(amount): Add experience, check if should level up
	- level_up(): Increase level, boost stats (attack +5, max_hp +20, etc), reset exp to 0
	- display_stats(): Show player's current level, exp, HP, stats in readable format
	- choose_action(): Return what player wants to do (attack, heal, etc) - can be simple input() for now

4. Design Notes:
	- Player should be customizable at creation (name, starting type)
	- Level scaling should follow a consistent formula (each level might cost 100 * level exp)
	- Stats should improve predictably when leveling (make it balanced)
"""
