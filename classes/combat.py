"""
COMBAT SYSTEM
=============
Orchestrates turn-based combat between player and enemies. Handles battle flow,
turn management, and determining victory/defeat conditions.

REQUIREMENTS:
1. Combat Manager Class:
	Central class that manages a single battle. Initialize with a player and an enemy.

	Attributes:
	- player (Player instance)
	- enemy (Enemy instance)
	- turn_count (int) - track number of turns
	- battle_log (list) - record of what happened each turn (for display)

2. Core Battle Methods:
	- start_battle(): Initialize battle, display opening
	- play_turn():
		* Get player action (attack, heal, etc)
		* Execute player action on enemy
		* Check if enemy is defeated -> return victory
		* Get enemy action via AI
		* Execute enemy action on player
		* Check if player is defeated -> return defeat
		* Display turn results (what happened)
	- end_battle(winner): Handle victory/defeat
		* If player wins: award experience/loot
		* Display summary

3. Battle Flow:
	- show_status(): Display both player and enemy HP/stats
	- log_action(message): Add to battle log for display
	- is_battle_over(): Check if either combatant is dead

4. Design Notes:
	- Each turn should be clearly shown to the player (what happened, HP changes)
	- Consider adding a battle log/history that can be displayed
	- Victory should award player experience based on enemy difficulty
	- This is the main game loop orchestrator for combat
"""
