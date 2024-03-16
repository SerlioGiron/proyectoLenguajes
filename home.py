from tkinter import *
import customtkinter
import raspaygana

root = customtkinter.CTk()
root.geometry("800x480")
root.title("Home")
root.anchor = CENTER


button = customtkinter.CTkButton( master=root, text="raspa y gana", command=raspaygana.main)
button2 = customtkinter.CTkButton( master=root, text="2")
button3 = customtkinter.CTkButton( master=root, text="3")
button4 = customtkinter.CTkButton( master=root, text="4")
button5 = customtkinter.CTkButton( master=root, text="5")


button.place(relx=0.5, rely=0.1, anchor=CENTER)
button2.place(relx=0.5, rely=0.25, anchor=CENTER)
button3.place(relx=0.5, rely=0.5, anchor=CENTER)
button4.place(relx=0.5, rely=0.75, anchor=CENTER)
button5.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()