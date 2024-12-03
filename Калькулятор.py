import os
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'

import tkinter as tk
from tkinter import messagebox

# Функция обработки нажатия кнопок
def on_button_click(symbol):
    current_text = entry.get()
    if symbol == "=":
        try:
            result = eval(current_text)  # Вычисление выражения
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception :
            messagebox.showerror("Ошибка", "Некорректное выражение")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")

# Поле ввода
entry = tk.Entry(root, width=25, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки
buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+"
]

# Расположение кнопок
row = 1
col = 0
for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(
        root, text=button, width=5, height=2, font=("Arial", 14), command=action
    ).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Запуск главного цикла программы
root.mainloop()


