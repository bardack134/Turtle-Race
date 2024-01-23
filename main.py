# Importa las clases Turtle y Screen del módulo turtle
import random

from turtle import Turtle, Screen

# Crea un objeto de la clase Screen
screen = Screen()

# Configura el tamaño de la pantalla a 500 de ancho y 400 de alto
screen.setup(width=500, height=400)

# Crea una lista con los colores de las tortugas
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Solicita al usuario que elija el color de la tortuga en la que apuesta
user_bet = screen.textinput(title="Make your bet", prompt="The turtles that are going to compete are of color red, orange, yellow, green, blue, purple. \n\nWhich turtle will win the race? Enter a color: ")

# Verifica que la elección del usuario esté en la lista de colores
while user_bet not in colors:    
    user_bet = screen.textinput(title="Make your bet", prompt="The turtles that are going to compete are of color red, orange, yellow, green, blue, purple. \n\nWhich turtle will win the race? Enter a color: ")

# Lista para almacenar objetos Turtle
list_of_turtles = []

# Posición vertical inicial de la primera tortuga
y = -150

# Bucle para crear tortugas de diferentes colores
for i in range(len(colors)):
    # Crea un objeto de la clase Turtle
    turtle = Turtle()
    
    # Cambia la forma de la tortuga a una tortuga
    turtle.shape("turtle")
    
    # Levanta el lápiz de la tortuga para que no deje trazo al moverse
    turtle.penup()
    
    # Mueve la tortuga a la posición (-240, y)
    turtle.goto(x=-240, y=y)
    
    # Cambia el color de la tortuga al color correspondiente de la lista
    turtle.color(colors[i])
    
    list_of_turtles.append(turtle)
    
    # Aumenta la posición vertical en 60 unidades para la siguiente tortuga
    y += 60

# Variable para verificar si la carrera ha terminado
finish = False

# Bucle principal para simular la carrera
while not finish:
    
    for i in range(len(list_of_turtles)):
        
        # Velocidad aleatoria para cada tortuga
        velocidad = random.randint(1, 8)
        
        # Tortugas corriendo hacia adelante a velocidades aleatorias
        list_of_turtles[i].forward(velocidad)

        # Verifica si alguna tortuga ha llegado a la meta
        if list_of_turtles[i].xcor() > 235:
            
            print("Finish")
            
            finish = True
            
            print(f"The winner turtle is {list_of_turtles[i].pencolor()}")
            
            # Verifica si la apuesta del usuario coincide con la tortuga ganadora
            if user_bet == list_of_turtles[i].pencolor():
                
                print("Excellent, you won!")
                
            else:
                
                print("Sorry, you lost.")
                
            break

# Permite que el programa continúe corriendo hasta que hagamos clic en la pantalla
# Debemos crear un objeto de la clase Screen() para usar el método exitonclick()
# Debe ir al final de nuestro código
# Cierra la ventana al hacer clic en la pantalla
screen.exitonclick()
