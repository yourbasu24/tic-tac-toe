import tkinter as tk
from tkinter import messagebox

# Initialize the game_board as a list
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Function to check for a win or a tie
def check_win():
    # Check for a win
    for combination in win_combinations:
        if all(game_board[i] == current_player for i in combination):
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            reset_game()
            return True

    # Check for a tie
    if " " not in game_board:
        messagebox.showinfo("Tie", "The game is a tie!")
        reset_game()
        return True

    return False

# Function to handle button click
def on_button_click(index):
    global current_player

    if game_board[index] == " ":
        game_board[index] = current_player
        buttons[index].config(text=current_player, state=tk.DISABLED, bg="red" if current_player == "O" else "blue")

        if not check_win():
            # Switch player
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player, game_board

    current_player = "X"
    game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    for button in buttons:
        button.config(text=" ", state=tk.NORMAL, bg="SystemButtonFace")

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define button positions
button_positions = [(i, j) for i in range(3) for j in range(3)]

# Create buttons
buttons = [tk.Button(root, text=" ", font=("Helvetica", 24), width=5, height=2, command=lambda i=i: on_button_click(i))
           for i, (row, col) in enumerate(button_positions)]

# Grid layout for buttons
for i, (row, col) in enumerate(button_positions):
    buttons[i].grid(row=row, column=col, padx=5, pady=5)

# Define winning combinations
win_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Initialize current player
current_player = "X"

# Run the main loop
root.mainloop()
