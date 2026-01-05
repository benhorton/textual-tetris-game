# Textual Tetris Game

A terminal-based implementation of the classic Tetris game using the [Textual](https://textual.textualize.io/) framework.

## Overview

This project creates an engaging, visually appealing Tetris experience that runs directly in the terminal. It leverages the Textual framework to provide a rich terminal user interface with colors, animations, and responsive controls.

## Features

- Complete Tetris game mechanics
  - All standard tetromino shapes (I, J, L, O, S, T, Z)
  - Rotation and movement
  - Line clearing
  - Increasing difficulty/speed
  - Score tracking
  - Game over detection

- Beautiful terminal user interface
  - Game board visualization
  - Score and level display
  - Next piece preview
  - Game controls display

- Intuitive keyboard controls
  - Arrow keys for movement
  - Rotation
  - Hard drop and soft drop
  - Hold piece functionality
  - Pause/resume game

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Clone the repository
git clone <repository-url>
cd textual-tetris-game

# Set up the project with uv
uv sync

# Run the game
uv run python -m textual_tetris_game
```

## Development

### Project Structure

```
textual-tetris-game/
├── pyproject.toml       # Project configuration
├── README.md            # Project documentation
├── src/
│   └── textual_tetris_game/
│       ├── __init__.py
│       ├── __main__.py  # Entry point
│       ├── cli.py       # Command-line interface
│       ├── game.py      # Game logic
│       └── ui.py        # User interface
└── tests/
    └── test_game.py     # Game logic tests
```

### Running Tests

```bash
pytest
```

## License

[MIT License](LICENSE)
