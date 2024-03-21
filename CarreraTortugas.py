# Documentación Turtle -> https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
from tkinter import messagebox
import random

def jugar():
    screen = Screen()
    screen.title("Carrera de tortugas")
    user = screen.textinput(title="Escoja un color", prompt=" ¿Quién ganará la carrera?\n   Tortugas: red, blue, green, yellow, purple, pink")
    colors = ["red", "blue", "green", "orange", "purple", "pink"]
    # Posiciones iniciales de las tortugas
    position_y = [-70, -40, -10, 20, 50, 80]
    screen.setup(width=500, height=400)
    turtles = []

    for position in range(0, 6):
        # Crear una nueva tortuga
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        # Asignar un color a cada tortuga
        new_turtle.color(colors[position])
        # Posicionar las tortugas en la línea de salida
        new_turtle.goto(x=-230, y=position_y[position])
        # Agregar la tortuga a la lista de tortugas
        turtles.append(new_turtle)

    # Iniciar la carrera de tortugas
    if user:
        game = True

    while game:
        # Mover cada tortuga
        for turtle in turtles:
            # Si la tortuga llega a la meta
            if turtle.xcor() > 230:
                game = False
                winner = turtle.pencolor()
                
                if winner == user:
                    seguir = messagebox.askyesno("", f"¡Ganaste! La tortuga {winner} es la ganadora.\n ¿Quieres jugar otra vez?")
                else:
                    seguir = messagebox.askyesno("", f"¡Perdiste! La tortuga {winner} es la ganadora.\n ¿Quieres jugar otra vez?")

                if not seguir:
                    screen.bye() # Cerrar la ventana
                    return  # Salir de la función jugar
                else:
                    screen.clear() # Limpiar la pantalla
                    return  # Salir de la función jugar

            rand_dist = random.randint(0, 10)
            turtle.forward(random.randint(0, 10))
        
    screen.exitonclick()

def main():
    while True:
        jugar()
