from colorama import Fore

from functions.utils import wipeTerminal

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
	def __init__(
		self, playerName: str = "playerCharacter", enemyName: str = "enemyCharacter"
	) -> None:
		self.player = Character(name=playerName, damageMultiplier=1.2, defense=0.91)  # type: ignore
		self.enemy = Character(name=enemyName)  # type: ignore

	def play(self) -> None:
		wipeTerminal()
		running = True
		while running:
			self.renderBattle()
			input("Press Enter to advance one turn")
			self.playRound()
			if self.player.isAlive() and self.enemy.isAlive():
				input("Press enter to play next round...")
			else:
				if not self.player.isAlive():
					running = False
					print("\nYou died...\n")
					input("Press enter to close the game...")
				else:
					running = False
					print("\nYou won...\n")
					input("Press enter to close the game...")

	def renderBattle(self) -> None:
		wipeTerminal()
		print(f"""{Fore.RED}{str(self.enemy)}{Fore.RESET}

{Fore.GREEN}{str(self.player)}{Fore.RESET}
""")

	def playRound(self) -> None:
		dealtDamage = self.player.attack(self.enemy)
		takenDamage = self.enemy.attack(self.player)
		print(
			f"You dealt {Fore.YELLOW}{dealtDamage}{Fore.RESET} and took {Fore.RED}{takenDamage}{Fore.RESET}"
		)
