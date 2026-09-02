"""
CHARACTER TYPES & WEAKNESS SYSTEM
==================================
Defines all possible character types and how they interact with each other.
This is NOT a class file, but a configuration/utility module.

REQUIREMENTS:
1. Type List/Enum:
	Define available character types. Suggested types:
	- FIRE: Strong against EARTH and ICE, weak to WATER
	- WATER: Strong against FIRE, weak to EARTH and LIGHTNING
	- EARTH: Strong against WATER and LIGHTNING, weak to FIRE
	- ICE: Strong against WATER, weak to FIRE
	- LIGHTNING: Strong against ICE and WATER, weak to EARTH
	- NEUTRAL: No advantages or disadvantages

2. Weakness/Strength Map:
	Create a data structure (dict or enum) that maps:
	TYPE_A attacking TYPE_B = multiplier

	Examples:
	- FIRE vs ICE = 1.5x damage (strong against)
	- FIRE vs WATER = 0.7x damage (weak against)
	- FIRE vs NEUTRAL = 1.0x damage (normal)

3. Lookup Functions:
	- get_type_effectiveness(attacker_type, defender_type): Return damage multiplier
	- is_strong_against(type_a, type_b): Return True if A is strong vs B
	- is_weak_against(type_a, type_b): Return True if A is weak vs B

4. Design Notes:
	- Make sure the type system is balanced (no type should be overpowered)
	- Consider rock-paper-scissors style balance (A beats B, B beats C, C beats A)
	- NEUTRAL should be a fallback type with no bonuses or penalties
	- This should be imported and used by Character.calculate_damage()
"""
