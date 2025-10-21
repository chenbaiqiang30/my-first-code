# Minesweeper Game

A classic Minesweeper game implementation in Python with command-line interface.

## Features

- Multiple difficulty levels (Easy, Medium, Hard, Custom)
- Flag cells to mark potential mines
- Automatic cell revelation for empty areas
- Clean command-line interface
- Win/lose detection

## How to Play

1. Run the game:
   ```bash
   python3 minesweeper.py
   ```

2. Select difficulty level:
   - **Easy**: 8x8 board with 10 mines
   - **Medium**: 10x10 board with 15 mines
   - **Hard**: 15x15 board with 30 mines
   - **Custom**: Choose your own settings

3. Game Commands:
   - `r <row> <col>` - Reveal a cell
   - `f <row> <col>` - Flag/unflag a cell (to mark mines)
   - `q` - Quit game

## Game Rules

- The goal is to reveal all cells that don't contain mines
- Numbers show how many mines are adjacent to that cell
- Use flags to mark cells you think contain mines
- If you reveal a mine, you lose
- Reveal all non-mine cells to win

## Example

```
  === MINESWEEPER ===

  Mines: 10
  Board: 8x8

     0  1  2  3  4  5  6  7
    ------------------------
 0 |  .  .  .  .  .  .  .  .
 1 |  .  .  .  .  .  .  .  .
 2 |  .  .  .  .  .  .  .  .
 3 |  .  .  .  .  .  .  .  .
 4 |  .  .  .  .  .  .  .  .
 5 |  .  .  .  .  .  .  .  .
 6 |  .  .  .  .  .  .  .  .
 7 |  .  .  .  .  .  .  .  .

Enter command: r 4 4
```

## Tips

- Start from corners or edges for better odds
- Use flags to keep track of known mines
- Numbers help you deduce where mines are located
- Empty cells (showing blank) automatically reveal adjacent cells

Enjoy playing!
