"""
ENEMY CLASS & ENEMY VARIATIONS
==============================
Base Enemy class extends Character with AI behavior. Then create specific enemy types
by creating subclasses or factory functions that configure enemies with different stats/types.

REQUIREMENTS:
1. Base Enemy Class (extends Character):
	- Inherits all character methods from Character
	- Additional attributes:
		* ai_strategy (str or method) - how enemy decides what to do (random, aggressive, heal)
		* loot_reward (dict) - experience and items enemy drops on defeat
		* difficulty (int) - used to scale stats

2. Base Enemy Methods:
	- choose_action(player): Determine what enemy does this turn (attack, heal, flee, etc)
		based on ai_strategy and current HP
	- get_loot(): Return loot_reward for player to collect
	- __str__(): Display enemy info

3. Enemy Variations (as Subclasses or Configured Instances):
	Create at least 3-4 enemy types. Examples:
	- Slime: Basic weak enemy (low HP, low attack, no type weakness)
	- FireSlime: Medium enemy with fire type (takes weakness from water types)
	- IceSlime: Medium enemy with ice type (takes weakness from fire types)
	- BossSlime: Stronger version (more HP, better AI, rare loot)

	For each variation, configure:
	- Base stats (HP, attack, defense)
	- Character type (from types.py)
	- AI behavior (how aggressive/smart)
	- Loot drops (experience and what items)

4. Design Notes:
	- Use composition/configuration over inheritance if possible (pass stats as constructor params)
	- AI strategy could be: "random action", "attack if healthy", "heal if low", "flee if critical"
	- Loot should be proportional to difficulty (harder enemy = more exp/better loot)
	- Different enemy types should have different strengths and weaknesses
"""
