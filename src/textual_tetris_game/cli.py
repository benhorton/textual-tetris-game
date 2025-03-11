"""
Textual Tetris Game - Command Line Interface

This module provides the command-line interface for the Textual Tetris Game.
It handles argument parsing and launches the main application.
"""

import sys
from typing import List, Optional

from textual_tetris_game.ui import TetrisApp


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the Textual Tetris Game.
    
    Args:
        argv: Command line arguments (defaults to sys.argv)
        
    Returns:
        Exit code
    """
    # In the future, we could add command-line arguments here
    # For now, we just launch the app
    app = TetrisApp()
    app.run()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
