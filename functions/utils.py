"""
Utility functions for the game

General helper functions used throughout the project.
"""

import os
import sys


def wipeTerminal() -> None:
	"""
	Clear the terminal screen in any environment.

	Works in:
	- macOS/Linux terminal
	- Windows Command Prompt/PowerShell
	- VS Code integrated terminal
	- Most other terminal emulators

	Returns: None
	"""
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
