#!/usr/bin/env python3
"""
Minesweeper Game - Command Line Version
A classic Minesweeper game implementation in Python
"""

import random
import os


class Minesweeper:
    """Minesweeper game class"""

    def __init__(self, rows=10, cols=10, mines=10):
        """
        Initialize the game

        Args:
            rows: Number of rows
            cols: Number of columns
            mines: Number of mines
        """
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flagged = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.won = False
        self.first_move = True

    def place_mines(self, exclude_row, exclude_col):
        """
        Place mines randomly on the board, excluding the first clicked cell

        Args:
            exclude_row: Row to exclude (first click)
            exclude_col: Column to exclude (first click)
        """
        mines_placed = 0
        while mines_placed < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            # Don't place mine on first clicked cell or if already has mine
            if (row == exclude_row and col == exclude_col) or self.board[row][col] == -1:
                continue

            self.board[row][col] = -1  # -1 represents a mine
            mines_placed += 1

        # Calculate numbers for each cell
        self.calculate_numbers()

    def calculate_numbers(self):
        """Calculate the number of adjacent mines for each cell"""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    continue

                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.board[nr][nc] == -1:
                                count += 1

                self.board[row][col] = count

    def reveal(self, row, col):
        """
        Reveal a cell and recursively reveal adjacent cells if needed

        Args:
            row: Row index
            col: Column index
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        if self.revealed[row][col] or self.flagged[row][col]:
            return

        # First move - place mines after first click
        if self.first_move:
            self.place_mines(row, col)
            self.first_move = False

        self.revealed[row][col] = True

        # Hit a mine
        if self.board[row][col] == -1:
            self.game_over = True
            return

        # If cell has no adjacent mines, reveal adjacent cells
        if self.board[row][col] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    self.reveal(row + dr, col + dc)

    def toggle_flag(self, row, col):
        """
        Toggle flag on a cell

        Args:
            row: Row index
            col: Column index
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return False

        if self.revealed[row][col]:
            return False

        self.flagged[row][col] = not self.flagged[row][col]
        return True

    def check_win(self):
        """Check if the player has won"""
        if self.first_move:
            return False

        for row in range(self.rows):
            for col in range(self.cols):
                # If a non-mine cell is not revealed, game not won
                if self.board[row][col] != -1 and not self.revealed[row][col]:
                    return False

        self.won = True
        self.game_over = True
        return True

    def display(self, show_mines=False):
        """
        Display the game board

        Args:
            show_mines: If True, show all mines (for game over)
        """
        os.system('clear' if os.name == 'posix' else 'cls')

        print("\n  === MINESWEEPER ===\n")
        print(f"  Mines: {self.mines}")
        print(f"  Board: {self.rows}x{self.cols}\n")

        # Column headers
        print("    ", end="")
        for col in range(self.cols):
            print(f"{col:2}", end=" ")
        print("\n    " + "-" * (self.cols * 3))

        # Display board
        for row in range(self.rows):
            print(f"{row:2} |", end=" ")
            for col in range(self.cols):
                if self.flagged[row][col] and not show_mines:
                    print(" F", end=" ")
                elif self.revealed[row][col] or show_mines:
                    if self.board[row][col] == -1:
                        print(" *", end=" ")
                    elif self.board[row][col] == 0:
                        print("  ", end=" ")
                    else:
                        print(f"{self.board[row][col]:2}", end=" ")
                else:
                    print(" .", end=" ")
            print()
        print()

    def play(self):
        """Main game loop"""
        print("\n=== Welcome to Minesweeper! ===\n")
        print("Commands:")
        print("  r <row> <col> - Reveal a cell")
        print("  f <row> <col> - Flag/unflag a cell")
        print("  q - Quit game\n")

        while not self.game_over:
            self.display()

            try:
                command = input("Enter command: ").strip().lower().split()

                if not command:
                    continue

                if command[0] == 'q':
                    print("\nThanks for playing!")
                    break

                if len(command) != 3:
                    print("Invalid command! Use: r/f <row> <col>")
                    input("Press Enter to continue...")
                    continue

                action = command[0]
                row = int(command[1])
                col = int(command[2])

                if action == 'r':
                    self.reveal(row, col)
                    if self.check_win():
                        self.display(show_mines=True)
                        print("Congratulations! You won!")
                        break
                elif action == 'f':
                    self.toggle_flag(row, col)
                else:
                    print("Invalid action! Use 'r' to reveal or 'f' to flag")
                    input("Press Enter to continue...")

            except (ValueError, IndexError):
                print("Invalid input! Please enter valid row and column numbers.")
                input("Press Enter to continue...")
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing!")
                break

        if self.game_over and not self.won:
            self.display(show_mines=True)
            print("Game Over! You hit a mine!")


def main():
    """Main function to start the game"""
    print("\n=== Minesweeper Game Setup ===\n")

    try:
        # Get difficulty level
        print("Select difficulty:")
        print("1. Easy (8x8, 10 mines)")
        print("2. Medium (10x10, 15 mines)")
        print("3. Hard (15x15, 30 mines)")
        print("4. Custom")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == '1':
            game = Minesweeper(8, 8, 10)
        elif choice == '2':
            game = Minesweeper(10, 10, 15)
        elif choice == '3':
            game = Minesweeper(15, 15, 30)
        elif choice == '4':
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            mines = int(input("Enter number of mines: "))

            if mines >= rows * cols:
                print("Too many mines! Using default settings.")
                game = Minesweeper(10, 10, 15)
            else:
                game = Minesweeper(rows, cols, mines)
        else:
            print("Invalid choice! Using medium difficulty.")
            game = Minesweeper(10, 10, 15)

        game.play()

    except KeyboardInterrupt:
        print("\n\nSetup interrupted. Exiting...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
