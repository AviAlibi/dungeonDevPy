"""
ARENA CLASS - STUDENT IMPLEMENTATION TEMPLATE
==============================================
Build this class to orchestrate turn-based combat between a player and enemy.

CORE CONCEPT:
	The Arena controls the game loop and coordinates between Character objects.
	It doesn't calculate damage (that's Character's job), it just manages flow.

WHAT YOU NEED TO BUILD:

1. __init__(playerName="playerCharacter", enemyName="enemyCharacter")
	- Create two Character instances (player and enemy)
	- Store them as self.player and self.enemy

2. play()
	- Clear terminal
	- Loop: renderBattle() → playRound() → check alive status
	- If both alive: pause for input
	- If player dead: show "You died...", pause, exit
	- If enemy dead: show "You won!", pause, exit

3. renderBattle()
	- Clear terminal with wipeTerminal()
	- Print enemy (one line)
	- Print blank line
	- Print player (one line)

4. playRound()
	- player attacks enemy: player.attack(enemy)
	- enemy attacks player: enemy.attack(player)
	- Print damage report: "You dealt X and took Y"

GUIDE FOR IMPLEMENTATION:
	1. Start by filling in __init__
	2. Write playRound next (simplest)
	3. Write renderBattle (uses existing methods)
	4. Write play (uses all three, add game loop logic)
	5. Run tests to verify each step

TESTS PROVIDED:
	Run this file to test each method as you implement it:
	$ python classes/arena.py
"""

try:
	from .character import Character
except ImportError:
	try:
		from ..answers.character import Character  # type: ignore
	except ImportError:
		try:
			from answers.character import Character  # type: ignore
		except ImportError:
			Character = None  # type: ignore


class Arena:
	"""
	Game arena that manages combat between two characters.

	Build the methods below following the specification in the docstring.
	"""

	def __init__(
		self,
		playerName: str = "playerCharacter",
		enemyName: str = "enemyCharacter",
	) -> None:
		"""
		Initialize the arena with a player and enemy.

		TODO: Create self.player and self.enemy as Character instances
		"""
		pass  # REPLACE THIS with your implementation

	def play(self) -> None:
		"""
		Run the main game loop until one combatant dies.

		TODO: Implement game loop that:
			1. Clears terminal
			2. Renders battle
			3. Plays one round
			4. Checks if game should continue
			5. Shows appropriate end message
		"""
		pass  # REPLACE THIS with your implementation

	def renderBattle(self) -> None:
		"""
		Display current battle state.

		TODO: Clear terminal and print player/enemy info
		"""
		pass  # REPLACE THIS with your implementation

	def playRound(self) -> None:
		"""
		Execute one round of combat.

		TODO: Have player attack enemy, enemy attack player, show results
		"""
		pass  # REPLACE THIS with your implementation


if __name__ == "__main__":
	print("=== Arena Class Tests ===\n")

	if Character is None:
		print("✗ Character class not found")
		print("  Implement: classes/character.py")
	else:
		print("Testing Arena implementation...\n")

		try:
			print("TEST 1: Can create Arena?")
			arena = Arena(playerName="Hero", enemyName="Goblin")
			print("  ✓ Arena created")
			print(f"  ✓ Player: {arena.player.name}")  # type: ignore
			print(f"  ✓ Enemy: {arena.enemy.name}")  # type: ignore
		except AttributeError as e:
			print(f"  ✗ Arena attributes missing: {e}")
		except Exception as e:
			print(f"  ✗ Failed: {e}")

		try:
			print("\nTEST 2: renderBattle() works?")
			arena = Arena(playerName="TestHero", enemyName="TestGoblin")
			print("  Calling renderBattle()...")
			arena.renderBattle()
			print("  ✓ renderBattle() executed (check output above)")
		except Exception as e:
			print(f"  ✗ Failed: {e}")

		try:
			print("\nTEST 3: playRound() works?")
			arena = Arena(playerName="Fighter", enemyName="Enemy")
			print(f"  Before: Player HP={arena.player.health}, Enemy HP={arena.enemy.health}")  # type: ignore
			arena.playRound()
			print(f"  After: Player HP={arena.player.health}, Enemy HP={arena.enemy.health}")  # type: ignore
			print("  ✓ playRound() executed (HPs should have changed)")
		except Exception as e:
			print(f"  ✗ Failed: {e}")

		try:
			print("\nTEST 4: Can simulate full combat?")
			arena = Arena(playerName="StrongHero", enemyName="WeakGoblin")
			rounds = 0
			maxRounds = 50

			while arena.player.isAlive() and arena.enemy.isAlive() and rounds < maxRounds:  # type: ignore
				arena.playRound()
				rounds += 1

			winner = "Player" if arena.player.isAlive() else "Enemy"  # type: ignore
			print(f"  ✓ Combat completed in {rounds} rounds")
			print(f"  ✓ {winner} won!")
			print(f"  ✓ Player HP: {arena.player.health}")  # type: ignore
			print(f"  ✓ Enemy HP: {arena.enemy.health}")  # type: ignore
		except Exception as e:
			print(f"  ✗ Failed: {e}")

	print("\n=== Tests Complete ===")
	print("\nNEXT STEPS:")
	print("1. Implement the pass statements with real code")
	print("2. Run tests after each method")
	print("3. When all tests pass, try: python main.py")
