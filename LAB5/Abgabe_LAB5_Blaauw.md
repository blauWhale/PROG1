# P05 – Lists, Tuples & File I/O

## 1.1 Trail Length
[Link to trail.py](./trail.py)

```python
import math

def path_length(trail):
    total_length = 0
    for i in range(1, len(trail)):
        x1, y1 = trail[i - 1]
        x2, y2 = trail[i]
        total_length += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_length

# Test mit dem Dreieckspfad
trail1 = [(1, 1), (2, 1), (1, 2), (1, 1)]
print("Total length of the triangular path:", path_length(trail1))

# Test mit dem Beispiel aus der Aufgabenstellung
trail2 = [
    (142.492, 208.536),
    (142.658, 207.060),
    (143.522, 205.978),
    (145.009, 205.546)
]
print("Total length of the example trail:", path_length(trail2))

```

## 1.3 Battleship
[Link to battleship.py](./battleship.py)

```python
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
```


## 2.1 Change File Extension
[Link to fileNameChanger.py](./fileNameChanger.py)


```python
import os

folder = r"C:\Users\rapha\OneDrive\ZHAW\2024HS\PROG1\music_extension_example"

for filename in os.listdir(folder):
    if filename.lower().endswith(".mp3"):
        os.rename(
            os.path.join(folder, filename),
            os.path.join(folder, filename.lower())
        )
```