"""
BASE CHARACTER CLASS
====================
This is the parent class for both Player and Enemy. It contains all shared functionality
that both character types need.

CORE ATTRIBUTES:
	- name (str): Character's name
	- maxHealth (float): Maximum health value, must be > 0
	- health (float): Current health, defaults to maxHealth, never goes below 0
	- damageMultiplier (float): Buff/debuff for damage (1.0 = normal, 1.1 = 10% more damage)
	- attackPower (float): Base damage dealt per attack
	- defense (float): Damage reduction multiplier (1.0 = take 100%, 0.5 = take 50%)

REQUIRED METHODS:

1. __init__(name, maxHealth=100.0, damageMultiplier=1.0, attackPower=10.0, defense=1.0)
	Logic:
		- Store all parameters as instance attributes
		- If maxHealth <= 0, set it to 1 (safety catch)
		- Set health equal to maxHealth on initialization
	Returns: None

2. takeDamage(num: float) -> float
	Parameters:
		- num: The base damage amount to take
	Logic:
		- Calculate actual damage: num * self.defense
		- If calculated damage <= 0, set to 0
		- Subtract damage from self.health
		- Health should never go below 0
	Returns: Current health after taking damage

3. heal(num: float) -> float
	Parameters:
		- num: The amount to heal
	Logic:
		- Only heal if num > 0
		- Add num to self.health
		- Cap health at maxHealth (never exceed it)
	Returns: Current health after healing

4. isAlive() -> bool
	Logic:
		- Check if health > 0
	Returns: True if alive, False if dead

5. calculateDamage() -> float
	Logic:
		- Calculate: attackPower * damageMultiplier
		- This is the base damage before applying to a target
	Returns: Damage amount as float

6. attack(target: Character) -> float
	Parameters:
		- target: Another Character instance to attack
	Logic:
		- Call calculateDamage() to get damage amount
		- Call target.takeDamage(damage)
		- This applies damage to the target
	Returns: The target's health after taking damage

7. __str__() -> str
	Logic:
		- Return a readable string representation of the character
		- Should include: name, current health, max health, attack power, defense
		- Format: "Name (HP: current/max, ATK: power, DEF: defense)" | Feel free to use the Colors class thats already pulled into this file, in order to make the output text look prettier
	Returns: String representation
"""

try:
	from ..answers.character import Character  # type: ignore
except ImportError:
	try:
		from answers.character import Character  # type: ignore
	except ImportError:
		Character = None  # type: ignore


if __name__ == "__main__":
	print("=== Character Class Basic Tests ===\n")

	if Character is None:
		print("✗ Character class not found. Make sure it's implemented.")
	else:
		try:
			print("1. Creating a character...")
			hero = Character(
				"Hero", maxHealth=100, attackPower=15, defense=1.0, damageMultiplier=1.0
			)
			print(f"✓ {hero}")
		except Exception as e:
			print(f"✗ Failed to create character: {e}")

		try:
			print("\n2. Testing calculateDamage()...")
			damage = hero.calculateDamage()  # type: ignore
			print(f"✓ Damage calculated: {damage}")
		except Exception as e:
			print(f"✗ Failed: {e}")

		try:
			print("\n3. Creating enemy and testing attack()...")
			enemy = Character(
				"Goblin", maxHealth=50, attackPower=8, defense=0.8, damageMultiplier=1.0
			)
			print(f"Before: {enemy}")
			hero.attack(enemy)  # type: ignore
			print(f"After:  {enemy}")
			print("✓ Attack successful")
		except Exception as e:
			print(f"✗ Failed: {e}")

		try:
			print("\n4. Testing takeDamage()...")
			initial_hp = hero.health  # type: ignore
			hero.takeDamage(20)  # type: ignore
			print(f"Took 20 damage: {initial_hp} -> {hero.health}")  # type: ignore
			print("✓ Damage taken")
		except Exception as e:
			print(f"✗ Failed: {e}")

		try:
			print("\n5. Testing heal()...")
			initial_hp = hero.health  # type: ignore
			hero.heal(10)  # type: ignore
			print(f"Healed 10: {initial_hp} -> {hero.health}")  # type: ignore
			print("✓ Healing works")
		except Exception as e:
			print(f"✗ Failed: {e}")

		try:
			print("\n6. Testing isAlive()...")
			print(f"Hero alive: {hero.isAlive()}")  # type: ignore
			enemy.takeDamage(100)  # type: ignore
			print(f"Enemy alive: {enemy.isAlive()}")  # type: ignore
			print("✓ isAlive() works")
		except Exception as e:
			print(f"✗ Failed: {e}")

		print("\n=== Tests Complete ===")
