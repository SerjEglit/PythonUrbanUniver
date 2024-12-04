import os
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'


import tkinter as tk
from tkinter import messagebox

# Основной класс игры
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")
        self.current_player = "X"  # Начинает игрок "X"
        self.board = [""] * 9  # Игровое поле, представленное списком
        self.buttons = []  # Кнопки для игрового поля
        self.create_board()

    # Создание игрового поля
    def create_board(self):
        for i in range(9):
            button = tk.Button(
                self.root, text="", font=("Arial", 24), width=5, height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    # Логика хода
    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():  # Если клетка пуста
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} выиграл!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    # Проверка победителя
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные
            (0, 4, 8), (2, 4, 6)              # Диагонали
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    # Сброс игры
    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()     