import tkinter as tk
from tkinter import messagebox

class NQueensUI:
    def __init__(self, master, n):
        self.master = master
        self.n = n
        self.board = [[0]*n for _ in range(n)]
        self.buttons = [[None]*n for _ in range(n)]
        self.create_board()

    def create_board(self):
        for i in range(self.n):
            for j in range(self.n):
                button = tk.Button(self.master, text=" ", width=4, height=2,
                                   command=lambda i=i, j=j: self.place_queen(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def place_queen(self, row, col):
        if self.board[row][col] == 0:
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.buttons[row][col].config(text="Q", fg="red")
                if self.check_win():
                    messagebox.showinfo("Congratulations", "You've successfully placed all queens!")
            else:
                messagebox.showwarning("Invalid Move", "This move is not allowed. The queen is under attack.")
        else:
            self.board[row][col] = 0
            self.buttons[row][col].config(text=" ")

    def is_safe(self, row, col):
        # Check this column
        for i in range(self.n):
            if self.board[i][col] == 1:
                return False

        # Check this row
        for j in range(self.n):
            if self.board[row][j] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower left diagonal
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        # Check lower right diagonal
        for i, j in zip(range(row, self.n), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def check_win(self):
        return sum(sum(row) for row in self.board) == self.n

if __name__ == "__main__":
    root = tk.Tk()
    root.title("N-Queens Solver")
    n = 8  # You can change this to any size of the board (4x4, 5x5, etc.)
    app = NQueensUI(root, n)
    root.mainloop()
