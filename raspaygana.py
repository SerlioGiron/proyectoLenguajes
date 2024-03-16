from tkinter import *
import customtkinter
import random

# global cont
cont = 0
historial = []

def on_button_click(button):
    global cont, historial
    cont += 1
    random_number = random.randint(1, 3)
    historial.append(random_number)
    # button.config(text="clicked")
    button.configure(fg_color="red", text = random_number)
    print("Button clicked")
    print(cont)
    if cont >= 3:
        print("Contador mayor a 3")
        if historial[0] == historial[1] == historial[2]:
            print("Ganaste")
        else:
            print("Perdiste")

def main(): 
    # Create instance of Tk
    root = customtkinter.CTk()
    root.geometry("800x480")
    root.title("Raspa y Gana")
    root.anchor = CENTER
    

    # # Create instance of customtkinter
    # ctk = customtkinter.CTk()

    button1 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button1))
    button2 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button2))
    button3 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button3))
    button4 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button4))
    button5 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button5))
    button6 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button6))
    button7 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button7))
    button8 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button8))
    button9 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button9))
    
    button1.place(relx=0.3, rely=0.25, anchor=CENTER)
    button2.place(relx=0.5, rely=0.25, anchor=CENTER)
    button3.place(relx=0.7, rely=0.25, anchor=CENTER)
    
    button4.place(relx=0.3, rely=0.5, anchor=CENTER)
    button5.place(relx=0.5, rely=0.5, anchor=CENTER)
    button6.place(relx=0.7, rely=0.5, anchor=CENTER)
    
    button7.place(relx=0.3, rely=0.75, anchor=CENTER)
    button8.place(relx=0.5, rely=0.75, anchor=CENTER)
    button9.place(relx=0.7, rely=0.75, anchor=CENTER)
    
    # cont = 0
    # while cont <= 3:
    #     print(cont)
    #     root.update()
    #     root.update_idletasks()
    #     # root.after(1000)
    
    # Start the Tk main loop
    
    root.mainloop()

if __name__ == "__main__":
    main()