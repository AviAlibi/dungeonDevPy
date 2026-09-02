"""
BASE CHARACTER CLASS
====================
This is the parent class for both Player and Enemy. It contains all shared functionality
that both character types need.

REQUIREMENTS:
1. Core Attributes:
	- name (str)
	- current_hp (int)
	- max_hp (int)
	- attack_power (int) - base damage dealt
	- defense (int) - reduces incoming damage
	- character_type (str) - from types.py (fire, ice, earth, lightning, etc)

2. Essential Methods:
	- __init__(): Initialize character with name, hp, attack, defense, type
	- take_damage(damage): Reduce HP, apply defense modifier, never go below 0
	- heal(amount): Increase HP, never exceed max_hp
	- is_alive(): Return True if HP > 0, False otherwise
	- calculate_damage(defender): Calculate damage output considering type matchups
		(should use the weakness system from types.py)
	- attack(target): Deal damage to another character (calls target.take_damage)
	- __str__(): Return character info (name, HP, type) for display

3. Design Notes:
	- This class should be abstract/template - both Player and Enemy inherit from it
	- Don't include player-specific things (exp, level) or enemy-specific things (AI, loot)
	- Defense should reduce damage taken (suggest formula like: damage_taken = damage * (1 - defense%))
	- Type weakness system should be integrated into calculate_damage()
"""
