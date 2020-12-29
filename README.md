# Conway-s-Game-of-Life
The “game” is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced “players”, by creating patterns with particular properties.

The universe of the Gme of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead.
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically or diagonally adjecent.
At each step in time (generation), the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on the next generation.
3. Any live cell with more than three live neighbours dies, as if by overcrowding
4. Any dead cell with exactly three live neigbours becomes a live cell, as if by reproduction

## Gameconfiguration

create a `game_config.json` file in the root of the project directory.
copy and paste the following content into that file.

    {
        "gridsize": 50,

        "settings": {
            "targetfps": 60,
            "sandbox": false
        }
    }

Play with the settings and see your universe unfold.

## Installation

Make sure you have python installed. Work from a virtual environment is always recommended.
To install the dependencies:

    python -m pip install -r requirements.txt

To start the game:

    python game.py

## Key-Binding

 - Q: Quits the game