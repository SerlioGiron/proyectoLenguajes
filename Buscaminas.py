import tkinter as tk
from tkinter import messagebox
import random
import time

class Buscaminas:
    DIFFICULTY_OPTIONS = {
        "Facil": {"rows": 9, "cols": 9, "bombs": 10},
        "Normal": {"rows": 13, "cols": 13, "bombs": 20},
        "Dificil": {"rows": 17, "cols": 17, "bombs": 30}
    }

    def __init__(self, master):
        self.master = master
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("Normal")
        self.difficulty_menu = tk.OptionMenu(self.master, self.difficulty_var, *self.DIFFICULTY_OPTIONS.keys(), command=self.update_difficulty)
        self.difficulty_menu.grid(row=0, column=0, columnspan=3, pady=5)

        
        self.rows, self.cols, self.bombs = self.DIFFICULTY_OPTIONS["Normal"].values()
        self.board = [[0] * self.cols for _ in range(self.rows)]
        self.discovered = [[False] * self.cols for _ in range(self.rows)]
        self.flags = [[False] * self.cols for _ in range(self.rows)]
        self.place_bombs()
        self.timer_label = tk.Label(self.master, text="Tiempo: 00:00")
        self.timer_label.grid(row=0, column=3, columnspan=3, pady=5)
        self.start_time = None
        self.create_widgets()
        self.update_timer()

    def create_widgets(self):
        for widget in self.master.winfo_children():
            if widget not in (self.difficulty_menu, self.timer_label):
                widget.destroy()
        self.buttons = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(self.master, width=2, height=1, bg="gray")
                button.grid(row=i+1, column=j, padx=0, pady=0, sticky='nsew')  # Offset by 1 row for the difficulty menu
                button.bind("<Button-1>", lambda event, row=i, col=j: self.on_left_click(row, col))
                button.bind("<Button-3>", lambda event, row=i, col=j: self.on_right_click(row, col))
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def place_bombs(self):
        bomb_spots = random.sample(range(self.rows * self.cols), self.bombs)
        for spot in bomb_spots:
            row = spot // self.cols
            col = spot % self.cols
            while self.board[row][col] == -1:
                spot = random.randint(0, self.rows * self.cols - 1)
                row = spot // self.cols
                col = spot % self.cols
            self.board[row][col] = -1

    def count_adjacent_bombs(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if self.board[i][j] == -1:
                    count += 1
        return count

    def on_left_click(self, row, col):
        if self.board[row][col] == -1:
            self.reveal_board()
            result = messagebox.showinfo("Has Perdido", "Perdistes!\nQuieres juegar otra vez?")
            if result == "ok":
                self.restart_game()
        else:
            if self.start_time is None:
                # Si es el primer clic, comenzar el temporizador
                self.start_timer()
            self.reveal_empty_cells(row, col)
            bombs_adjacent = self.count_adjacent_bombs(row, col)
            self.buttons[row][col].config(text=str(bombs_adjacent), bg="light gray")
            self.discovered[row][col] = True
            if self.check_win():
                result = messagebox.showinfo("Has Ganado", "Ganastes!\nQuieres jugar otra vez?")
                if result == "ok":
                    self.restart_game()
    
    def reveal_empty_cells(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.discovered[row][col]:
            return
        bombs_adjacent = self.count_adjacent_bombs(row, col)
        self.buttons[row][col].config(text=str(bombs_adjacent), bg="light gray")
        self.discovered[row][col] = True
        if bombs_adjacent == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    self.reveal_empty_cells(i, j)

    def on_right_click(self, row, col):
        if not self.discovered[row][col]:
            if self.flags[row][col]:
                self.buttons[row][col].config(text="")
                self.flags[row][col] = False
            else:
                self.buttons[row][col].config(text="🚩")
                self.flags[row][col] = True

    def check_win(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != -1 and not self.discovered[i][j]:
                    return False
        return True

    def reveal_board(self):
        self.start_time = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    self.buttons[i][j].config(text="💣", bg='red')

    def restart_game(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(text="", bg='SystemButtonFace', state="normal")
                self.flags[i][j] = False
                self.board[i][j] = 0
                self.discovered[i][j] = False
        timer_text = f"Tiempo: 00:00"
        self.timer_label.config(text=timer_text)
        self.create_widgets()
        self.place_bombs()

    def update_difficulty(self, event=None):
        difficulty = self.difficulty_var.get()
        self.rows, self.cols, self.bombs = self.DIFFICULTY_OPTIONS[difficulty].values()
        self.board = [[0] * self.cols for _ in range(self.rows)]
        self.discovered = [[False] * self.cols for _ in range(self.rows)]
        self.flags = [[False] * self.cols for _ in range(self.rows)]
        self.start_time = None
        timer_text = f"Tiempo: 00:00"
        self.timer_label.config(text=timer_text)
        self.create_widgets()
        self.place_bombs()

    def start_timer(self):
        self.start_time = time.time()

    def update_timer(self):
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            timer_text = f"Tiempo: {minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_text)
        self.master.after(1000, self.update_timer)

def main():
    root = tk.Tk()
    root.title("Buscaminas")
    game = Buscaminas(root)
    root.mainloop()

if __name__ == "__main__":
    main()