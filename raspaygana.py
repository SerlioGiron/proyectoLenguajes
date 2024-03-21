from tkinter import *
import customtkinter
import random

# global cont
# comentario
cont = 0
historial = []
botones = []

def reiniciar():
    global botones, cont, historial
    print("Reiniciando")
    cont = 0
    # color = boton.cget(color)
    for boton in botones:
        boton.configure(text="", fg_color="lightblue")

def on_button_click(button):
    global cont, historial, root
    cont += 1
    random_number = random.randint(1, 3)
    print("numero > ", random_number)
    historial.append(random_number)
    # button.config(text="clicked")
    button.configure(fg_color="red", text = random_number)
    print("Button clicked")
    print(cont)
    
    if cont == 2 and historial[0] != historial[1]:
        reiniciar()
        historial.clear()
        print("Perdiste")
        WindowLose = customtkinter.CTk()
        WindowLose.anchor = CENTER
        pantWin = customtkinter.CTkLabel(master=WindowLose, text="Perdiste", fg_color="red")
        pantWin.place(relx=0.5, rely=0.5, anchor=CENTER)
        WindowLose.mainloop()
    
    if cont >= 3:
        for numero in historial:
            print( "numero -> ",numero)
        reiniciar()
        print("Contador mayor a 3")
        if historial[0] == historial[1] == historial[2]:
            historial.clear()
            print("Ganaste")
            WindowWin = customtkinter.CTk()
            WindowWin.anchor = CENTER
            pantWin = customtkinter.CTkLabel(master=WindowWin, text="Ganaste", fg_color="green")
            pantWin.place(relx=0.5, rely=0.5, anchor=CENTER)
            WindowWin.mainloop()
            
            # root.destroy()
        else:
            historial.clear()
            print("Perdiste")
            WindowLose = customtkinter.CTk()
            WindowLose.anchor = CENTER
            pantWin = customtkinter.CTkLabel(master=WindowLose, text="Perdiste", fg_color="red")
            pantWin.place(relx=0.5, rely=0.5, anchor=CENTER)
            WindowLose.mainloop()
            
            # root.destroy()
            
            


def main(): 
    # Create instance of Tk
    root = customtkinter.CTk()
    root.geometry("800x480")
    root.title("Raspa y Gana")
    root.anchor = CENTER
    

    # # Create instance of customtkinter
    # ctk = customtkinter.CTk()
    global botones

    button1 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button1), fg_color="lightblue")
    botones.append(button1)
    button2 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button2), fg_color="lightblue")
    botones.append(button2)
    button3 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button3), fg_color="lightblue")
    botones.append(button3)
    button4 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button4), fg_color="lightblue")
    botones.append(button4)
    button5 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button5), fg_color="lightblue")
    botones.append(button5)
    button6 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button6), fg_color="lightblue")
    botones.append(button6)
    button7 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button7), fg_color="lightblue")
    botones.append(button7)
    button8 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button8), fg_color="lightblue")
    botones.append(button8)
    button9 = customtkinter.CTkButton( master=root, text="", command=lambda: on_button_click(button9), fg_color="lightblue")
    botones.append(button9)
    
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