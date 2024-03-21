import tkinter as tk
from tkinter import messagebox
import random

class WordleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle")

        self.words = ["apple", "table", "chair", "smile", "brain", "house", "happy", "candy", "beach", "dream"]
        self.secret_word = random.choice(self.words)
        print("Secret word:", self.secret_word) 
        self.attempts_left = 5
        self.current_attempt = 0

        self.draw_word_display()
        self.draw_input_grid()
        self.draw_attempts_display()

    def draw_word_display(self):
        self.word_display = tk.Label(self.master, text=" ".join(["_" for _ in range(5)]), font=('Arial', 16))
        self.word_display.pack(pady=10)

    def draw_input_grid(self):
        self.input_entries = []
        frame = tk.Frame(self.master)
        frame.pack()
        for i in range(5):
            row_entries = []
            for j in range(5):
                entry = tk.Entry(frame, width=3, font=('Arial', 16), state='normal' if i == 0 else 'disabled')
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.input_entries.append(row_entries)

    def draw_attempts_display(self):
        self.attempts_display = tk.Label(self.master, text=f"Attempts Left: {self.attempts_left}", font=('Arial', 14))
        self.attempts_display.pack(pady=5)

    def check_guess(self):
        if self.attempts_left == 0:
            messagebox.showinfo("Game Over", "You've run out of attempts.")
            return

        print("Checking grid lines:")
        current_row = self.input_entries[self.current_attempt]
        for i, entry in enumerate(current_row):
            print(f"Row {self.current_attempt + 1}, Column {i + 1}: {entry.get()}")
            if not entry.get():
                messagebox.showerror("Incomplete Guess", "Please fill all grids in the current row.")
                return

        attempt = "".join(entry.get().lower() for entry in current_row)
        if len(attempt) != 5 or not attempt.isalpha():
            messagebox.showerror("Invalid Guess", "Please enter a valid five-letter word.")
            return

        print("Current attempt:", attempt)

        self.current_attempt += 1

        if attempt == self.secret_word:
            self.word_display.config(text=self.secret_word.upper(), fg='green')
            messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
            self.disable_input_entries()
        else:
            self.attempts_left -= 1
            self.attempts_display.config(text=f"Attempts Left: {self.attempts_left}")
            if self.attempts_left == 0:
                self.word_display.config(text=self.secret_word.upper(), fg='red')
                messagebox.showinfo("Game Over", f"You've run out of attempts. The word was {self.secret_word}.")
                self.disable_input_entries()
            else:
                self.update_word_display(attempt)  
                self.enable_next_attempt()  

        for entry in current_row:
            entry.delete(0, tk.END)

    def restart_game(self):
        self.secret_word = random.choice(self.words)
        print("Secret word:", self.secret_word)
        self.attempts_left = 5
        self.current_attempt = 0

        for row_entries in self.input_entries:
            for entry in row_entries:
                entry.delete(0, tk.END)
                entry.config(state='normal' if row_entries == self.input_entries[0] else 'disabled')

        self.word_display.config(text=" ".join(["_" for _ in range(5)]), fg='black')

        self.attempts_display.config(text=f"Attempts Left: {self.attempts_left}")

    def update_word_display(self, guess):
        revealed_letters = [letter if letter == self.secret_word[i] else "_" for i, letter in enumerate(guess)]
        self.word_display.config(text=" ".join(revealed_letters))

    def disable_input_entries(self):
        for row_entries in self.input_entries:
            for entry in row_entries:
                entry.config(state='disabled')

    def enable_next_attempt(self):
        if self.current_attempt < 5: 
            current_row_entries = self.input_entries[self.current_attempt]
            current_row_values = [entry.get() for entry in current_row_entries]
            next_row = self.input_entries[self.current_attempt]
            
            for row_entries in self.input_entries:
                for entry in row_entries:
                    entry.config(state='disabled')

            for entry in next_row:
                entry.config(state='normal')

            #self.current_attempt += 1|

            for entry, value in zip(current_row_entries, current_row_values):
                entry.delete(0, tk.END)
                entry.insert(0, value)

def main():
    root = tk.Tk()
    wordle_game = WordleGame(root)
    check_button = tk.Button(root, text="Check", command=wordle_game.check_guess)
    check_button.pack(pady=5)
    restart_button = tk.Button(root, text="Restart", command=wordle_game.restart_game)
    restart_button.pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    main()