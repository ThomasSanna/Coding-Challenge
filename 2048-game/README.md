# 2048 Game in Python - Challenge n°6 by WadeeKT
## This Python script implements the classic 2048 game using the curses library for the command-line interface.

### Requirements
Python 3
NumPy
curses (usually included in Python standard library)
### How to Play
1. Run the script.
2. Use arrow keys (UP, DOWN, LEFT, RIGHT) to move the tiles in the corresponding direction.
3. The game automatically adds a new random tile (2, 4, or 8) after each move.
4. Tiles with the same value merge when they collide.
### Game Logic
- The game is played on a 4x4 grid.
- The goal is to reach the 2048 tile by merging tiles with the same value.
- The game ends when the grid is full, and no more moves are possible.
### Customization
- You can modify the valWeights and valEndRound variables to change the probabilities and values of new tiles.
- Feel free to experiment with the code to add more features or customize the game further.

Enjoy playing 2048!