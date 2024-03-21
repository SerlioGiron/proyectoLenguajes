import tkinter as tk
from tkinter import messagebox
import random
import copy
import time

class SudokuGrid:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        
        self.grid_size = 9
        self.grid = [[0]*self.grid_size for _ in range(self.grid_size)]
        self.user_input = {} 
        
        self.generate_sudoku()
        self.draw_grid()
        self.draw_timer()
        self.draw_solution_button()
        self.draw_check_button()
        
        self.start_time = time.time()
        self.update_timer()
        self.timer_id = None
        
    def generate_sudoku(self):
        for i in range(0, self.grid_size, 3):
            self.fill_box(i, i)

        self.solve_sudoku(0, 0)
        self.solution = copy.deepcopy(self.grid)
        self.remove_numbers()
        
    def fill_box(self, row, col):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.grid[row+i][col+j] = nums.pop()
                
    def solve_sudoku(self, row, col):
        if row == self.grid_size - 1 and col == self.grid_size:
            return True
        
        if col == self.grid_size:
            row += 1
            col = 0
            
        if self.grid[row][col] != 0:
            return self.solve_sudoku(row, col + 1)
        
        for num in range(1, self.grid_size + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve_sudoku(row, col + 1):
                    return True
                self.grid[row][col] = 0
                
        return False
    
    def is_valid(self, row, col, num):
        for x in range(self.grid_size):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False
            
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True
    
    def remove_numbers(self):
        num_to_remove = 40  
        for _ in range(num_to_remove):
            row, col = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            self.grid[row][col] = 0
                
    def draw_grid(self):
        self.entries = []
        for i in range(self.grid_size):
            row_entries = []
            for j in range(self.grid_size):
                cell_value = self.user_input.get((i, j), self.grid[i][j]) 
                if cell_value != 0:
                    entry = tk.Entry(self.master, width=2, font=('Arial', 16), justify="center", fg='green')
                    entry.insert(tk.END, str(cell_value))
                    entry.config(state=tk.DISABLED)
                else:
                    entry = tk.Entry(self.master, width=2, font=('Arial', 16), justify="center")
                    entry.bind('<KeyRelease>', lambda event, row=i, col=j: self.on_entry_keypress(event, row, col))
                    entry.bind('<FocusIn>', lambda event, row=i, col=j: self.on_entry_focus_in(event, row, col))
                    entry.bind('<FocusOut>', lambda event, row=i, col=j: self.on_entry_focus_out(event, row, col))
                entry.grid(row=i, column=j)
                row_entries.append(entry)
                
                if i % 3 == 0 and i != 0:
                    entry.grid(pady=(2, 0))
                if j % 3 == 0 and j != 0:
                    entry.grid(padx=(2, 0))
                    
            self.entries.append(row_entries)

    def on_entry_focus_in(self, event, row, col):
        for entry in self.entries[row]:
            entry.config(bg='#B0C4DE') 
        for i in range(self.grid_size):
            self.entries[i][col].config(bg='#B0C4DE')
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == 0:
                    self.entries[i + start_row][j + start_col].config(bg='#B0C4DE')  

    def on_entry_focus_out(self, event, row, col):
        for entry in self.entries[row]:
            entry.config(bg='white')
        for i in range(self.grid_size):
            self.entries[i][col].config(bg='white')
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                self.entries[i + start_row][j + start_col].config(bg='white')
        
        if self.check_win():
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            messagebox.showinfo("Sudoku",f"Ganó! Lo logró en {minutes} minutos y {seconds} segundos!")
            self.master.after_cancel(self.timer_id)
                
    def draw_timer(self):
        self.timer_label = tk.Label(self.master, text="Tiempo: 00:00", font=('Arial', 16))
        self.timer_label.grid(row=self.grid_size, columnspan=self.grid_size, padx=10, pady=5)

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        self.timer_label.config(text=f"Tiempo: {minutes:02d}:{seconds:02d}")
        self.timer_id = self.master.after(1000, self.update_timer)
                
    def on_entry_keypress(self, event, row, col):
        if event.char.isdigit():
            entry = self.entries[row][col]
            entry.delete(0, tk.END)
            entry.insert(tk.END, event.char)
            self.user_input[(row, col)] = int(event.char) 
            if self.validate_input(row, col, int(event.char)):
                entry.config(fg='green')
            else:
                entry.config(fg='red')
        return 'break'
    
    def validate_input(self, row, col, num):
        return self.solution[row][col] == num
                
    def print_solution(self):
        messagebox.showinfo("Sudoku", "Se rindió! Aquí está la solución.")
        solucion = "Solución:\n"
        for row in self.solution:
            solucion += ' '.join(map(lambda x: f"{x} ", row)) + '\n'
        messagebox.showinfo("Sudoku", solucion)
        self.reset_game()

    def reset_game(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.user_input[(i, j)] = 0
        self.start_time = time.time()
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None  # Reset the timer ID
        self.update_timer()
        self.master.destroy()
        main()


    def get_row(self, row):
        return self.grid[row]

    def get_column(self, col):
        return [self.grid[row][col] for row in range(self.grid_size)]

    def get_box(self, row, col):
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        return [self.grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]
    
    def draw_solution_button(self):
        self.solution_button = tk.Button(self.master, text="Rendirse", command=self.print_solution)
        self.solution_button.grid(row=self.grid_size + 1, columnspan=self.grid_size, padx=10, pady=5)

    def check_win(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell_value = self.user_input.get((row, col), self.grid[row][col])  
                if cell_value != self.solution[row][col]:
                    return False
        return True
    
    def draw_check_button(self):
        self.check_button = tk.Button(self.master, text="Check", command=self.check_win_button_click)
        self.check_button.grid(row=self.grid_size + 2, columnspan=self.grid_size, padx=10, pady=5)

    def check_win_button_click(self):
        if self.check_win():
            messagebox.showinfo("Sudoku","Ganó!")
        else:
            messagebox.showinfo("Sudoku","Siga Intentando!")

def main():
    root = tk.Tk()
    sudoku_grid = SudokuGrid(root)
    root.mainloop()

if __name__ == "__main__":
    main()