import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
root = Tk()
root.withdraw()
global letters_images, hangman_images
score = 0
hangman_dir = os.path.dirname(os.path.abspath(__file__))
#letters icon
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters_images = {let: ImageTk.PhotoImage(Image.open(os.path.join(hangman_dir, f"HangmanRecursosImportantes\\{let}.png"))) for let in al}

# hangman images
h123 = ['h1','h2','h3','h4','h5','h6','h7']
hangman_images = {hangman: PhotoImage(file=f"HangmanRecursosImportantes\\{hangman}.png") for hangman in h123}
def restart_game():
    for widget in root.winfo_children():
        widget.destroy()
    main()
def finish_game():
    for widget in root.winfo_children():
        widget.destroy()
    root.withdraw()
def main():
    root.deiconify()
    global score
    run = True
    # main loop
    while run:
        if root.winfo_width() != 905 or root.winfo_height() != 700:
            root.geometry('905x700')
        root.title('HANG MAN')
        root.config(bg = '#E7FFFF')
        count = 0
        win_count = 0

        # choosing word
        index = random.randint(0,853)
        with open('HangmanRecursosImportantes\\words.txt','r') as file:
            l = file.readlines()
        selected_word = l[index].strip('\n')

        # creation of word dashes variables
        x = 250
        d = []
        for i in range(len(selected_word)):
            x += 40
            d.append(Label(root,text="_",bg="#E7FFFF",font=("arial",20)))
            d[-1].place(x=x,y=450)
        #letters placement
        button = [['b1','a',0,525],['b2','b',70,525],['b3','c',140,525],['b4','d',210,525],['b5','e',280,525],['b6','f',350,525],['b7','g',420,525],['b8','h',490,525],['b9','i',560,525],['b10','j',630,525],['b11','k',700,525],['b12','l',770,525],['b13','m',840,525],['b14','n',0,575],['b15','o',70,575],['b16','p',140,575],['b17','q',210,575],['b18','r',280,575],['b19','s',350,575],['b20','t',420,575],['b21','u',490,575],['b22','v',560,575],['b23','w',630,575],['b24','x',700,575],['b25','y',770,575],['b26','z',840,575]]

        buttons = []
        for q1 in button:
            buttons.append(Button(root, bd=0, command=lambda q1=q1: check(q1[1], q1[0]), bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=letters_images[q1[1]]))
            buttons[-1].place(x=q1[2],y=q1[3])

        #hangman placement
        han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
        hangman_labels = []
        for p1 in han:
            hangman_labels.append(Label(root,bg="#E7FFFF",image=hangman_images[p1[1]]))

        # placement of first hangman image
        hangman_labels[0].place(x = 300,y =- 50)

        # exit button
        def close():
            nonlocal run
            answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
            if answer == True:
                run = False
                finish_game()

        e1 = ImageTk.PhotoImage(file = 'HangmanRecursosImportantes\\exit.png')
        ex = Button(root,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
        ex.place(x=770,y=10)
        s2 = 'SCORE:'+str(score)
        s1 = Label(root,text = s2,bg = "#E7FFFF",font = ("arial",25))
        s1.place(x = 10,y = 10)

        # button press check function
        def check(letter,button):
            nonlocal count,win_count,run
            global score
            buttons[int(button[1:]) - 1].destroy()
            if letter in selected_word:
                for i in range(len(selected_word)):
                    if selected_word[i] == letter:
                        win_count += 1
                        d[i].config(text=letter.upper())
                if win_count == len(selected_word):
                    score += 1
                    answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                    if answer == True:
                        restart_game()
                    else:
                        run = False
                        finish_game()
            else:
                count += 1
                hangman_labels[count-1].destroy()
                hangman_labels[count].place(x=300,y=-50)
                if count == 6:
                    answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                    if answer == True:
                        score = 0
                        restart_game()
                    else:
                        run = False
                        finish_game()     
        root.mainloop()

if __name__ == "__main__":
    main()