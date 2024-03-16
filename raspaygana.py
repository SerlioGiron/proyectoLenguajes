from tkinter import *
import customtkinter

cont = 0

def on_button_click(button):
    cont = cont + 1
    # button.config(text="clicked")
    button.configure(fg_color="red")
    print("Button clicked")
    print(cont)

def main(): 
    # Create instance of Tk
    root = customtkinter.CTk()
    root.geometry("800x480")
    root.title("Raspa y Gana")
    root.anchor = CENTER
    

    # # Create instance of customtkinter
    # ctk = customtkinter.CTk()

    button1 = customtkinter.CTkButton( master=root, text="1", command=lambda: on_button_click(button1))
    button2 = customtkinter.CTkButton( master=root, text="2", command=lambda: on_button_click(button2))
    button3 = customtkinter.CTkButton( master=root, text="3", command=lambda: on_button_click(button3))
    button4 = customtkinter.CTkButton( master=root, text="4", command=lambda: on_button_click(button4))
    button5 = customtkinter.CTkButton( master=root, text="5", command=lambda: on_button_click(button5))
    button6 = customtkinter.CTkButton( master=root, text="6", command=lambda: on_button_click(button6))
    button7 = customtkinter.CTkButton( master=root, text="7", command=lambda: on_button_click(button7))
    button8 = customtkinter.CTkButton( master=root, text="8", command=lambda: on_button_click(button8))
    button9 = customtkinter.CTkButton( master=root, text="9", command=lambda: on_button_click(button9))
    
    button1.place(relx=0.3, rely=0.25, anchor=CENTER)
    button2.place(relx=0.5, rely=0.25, anchor=CENTER)
    button3.place(relx=0.7, rely=0.25, anchor=CENTER)
    
    button4.place(relx=0.3, rely=0.5, anchor=CENTER)
    button5.place(relx=0.5, rely=0.5, anchor=CENTER)
    button6.place(relx=0.7, rely=0.5, anchor=CENTER)
    
    button7.place(relx=0.3, rely=0.75, anchor=CENTER)
    button8.place(relx=0.5, rely=0.75, anchor=CENTER)
    button9.place(relx=0.7, rely=0.75, anchor=CENTER)
    
    # Start the Tk main loop
    root.mainloop()

if __name__ == "__main__":
    main()