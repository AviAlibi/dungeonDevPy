"""
Main entry point for the Dungeon Game

Handles initialization and graceful fallback if classes are not yet implemented.
"""

try:
	from classes.arena import Arena  # type: ignore
except ImportError:
	try:
		from answers.arena import Arena  # type: ignore
	except ImportError:
		Arena = None  # type: ignore


if __name__ == "__main__":
	if Arena is None:
		print("✗ Arena class not found.")
		print("  Please implement the Arena class in:")
		print("  - classes/arena.py (preferred)")
		print("  - or answers/arena.py (fallback)")
	else:
		try:
			game = Arena(playerName=input("Player Name: "), enemyName="Goblin")
			game.play()
		except Exception as e:
			print(f"✗ Game crashed: {e}")
			import traceback

			traceback.print_exc()
