fo("Sudoku", "Se rindió! Aquí está la solución.")
        solucion = "Solución:\n"
        for row in self.solution:
            solucion += ' '.join(map(lambda x: f"{x} ", row)) + '\n'
        messagebox.showinfo("Sudoku", solucion)
        self.reset_game()