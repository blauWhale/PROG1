import random

# Create the board
board = [["O"] * 10 for _ in range(15)]

# Place the ship randomly
ship_row, ship_col = random.randint(0, 14), random.randint(0, 9)

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Main game loop
for turn in range(10):
    print(f"Turn {turn + 1}")
    print_board(board)
    try:
        guess_row = int(input("Guess row (0-14): "))
        guess_col = int(input("Guess column (0-9): "))
        if guess_row == ship_row and guess_col == ship_col:
            print("You hit the ship! You win!")
            break
        elif 0 <= guess_row < 15 and 0 <= guess_col < 10:
            board[guess_row][guess_col] = "X"
        else:
            print("Out of bounds. Try again.")
    except ValueError:
        print("Invalid input. Enter numbers only.")
else:
    print("Game over. You ran out of turns.")
    print(f"The ship was at ({ship_row}, {ship_col}).")
