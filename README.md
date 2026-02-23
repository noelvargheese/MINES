# Python Basic Pac-Man

A simplified, grid-based clone of the classic Pac-Man game, implemented using Python's built-in `tkinter` module. This project demonstrates basic graphical user interfaces (GUI), event-driven programming, and game loops using standard library features without any exterior dependencies.

## Features
- **Grid-based Movement**: Fluid control of Pac-Man with turn queueing using arrow keys or WASD.
- **Classic Mechanisms**: Dots to collect, walls for collision, and ghosts that chase the player.
- **Basic Ghost AI**: Ghosts will move towards Pac-Man using Manhattan distance, with a slight randomness to avoid clumping together permanently.
- **Progressing Difficulty**: Leveling up increases the game speed slightly and rotates the color theme of the maze.
- **Score & Level Tracking**: Your run will be tracked across levels!
- **Pause & Resume**: Users can pause the game loop hitting 'P' or using the UI buttons.

## Requirements
- **Python 3.x**
- **Tkinter** (usually included by default within standard Python installations).

## How to play
1. Run `python MINE.py` from your terminal or IDE.
2. Click **Start Game** on the Home Screen.
3. Use the **Arrow Keys** or **W, A, S, D** to traverse the maze.
4. Reach zero dots to complete the level!
5. Avoid the ghosts; any collision results in a Game Over.

## File Structure
- `MINE.py`: Contains the complete game code spanning from the main `App` class encapsulating the Tk application, to the `HomeScreen` and `GameScreen` view implementations.

# MINES
