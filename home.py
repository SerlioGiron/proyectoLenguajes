from tkinter import *
import customtkinter
import raspaygana
import sudoku
import CarreraTortugas
import hangman
import wordle
import Buscaminas


def main(): 
    root = customtkinter.CTk()
    root.geometry("800x400")
    root.title("Home")
    root.anchor = CENTER
    button = customtkinter.CTkButton( master=root, text="Raspa y Gana", command=raspaygana.main)
    button2 = customtkinter.CTkButton( master=root, text="Sudoku", command=sudoku.main)
    button3 = customtkinter.CTkButton( master=root, text="Carrera de Tortugas", command=CarreraTortugas.main)
    button4 = customtkinter.CTkButton( master=root, text="Buscaminas", command=Buscaminas.main)
    button5 = customtkinter.CTkButton(master=root, text="Hangman", command=hangman.main)
    button6 = customtkinter.CTkButton(master=root, text="Wordle", command=wordle.main)
    button.place(relx=0.5, rely=0.1, anchor=CENTER)
    button2.place(relx=0.5, rely=0.25, anchor=CENTER)
    button3.place(relx=0.5, rely=0.5, anchor=CENTER)
    button6.place(relx=0.5, rely=0.6, anchor=CENTER)
    button4.place(relx=0.5, rely=0.75, anchor=CENTER)
    button5.place(relx=0.5, rely=0.9, anchor=CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()