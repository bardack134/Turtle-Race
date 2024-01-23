# Importa las clases Turtle y Screen del módulo turtle
from turtle import Turtle, Screen

# Crea un objeto de la clase Screen
screen=Screen()

# Configura el tamaño de la pantalla a 500 de ancho y 400 de alto
screen.setup(width=500, height=400)


# user_bet = screen.textinput(title="make your bet ", prompt="The turtles that are going to compete are of color red, orange, yellow, green, blue, purple. \n\n Which turtle will win the race? Enter a color: ")

# print(user_bet)

# Crea una lista con los colores de las tortugas
colors=["red", "orange", "yellow", "green", "blue", "purple"]

list_of_turtles=[]

# Crea una variable para guardar la posición vertical inicial de la primera tortuga
y=-150


# Crea un bucle que se repite tantas veces como elementos hay en la lista de colores
for i in range(0, len(colors)):
    
    # Crea un objeto de la clase Turtle
    turtle=Turtle()
    
    # Cambia la forma de la tortuga a una tortuga
    turtle.shape("turtle")
    
    # Levanta el lápiz de la tortuga para que no deje trazo al moverse
    turtle.penup()
    
    # Mueve la tortuga a la posición (-240, y)
    turtle.goto(x=-240, y=y)
    
    # Cambia el color de la tortuga al color correspondiente de la lista
    turtle.color(colors[i])
        
    list_of_turtles.append(turtle)
    
    # print(list_of_turtles)
    
    # Aumenta la posición vertical en 60 unidades para la siguiente tortuga
    y += 60
    
    if i == 5:
        print(len(list_of_turtles))
        
        finish=False
        
        while finish==False:
            
            list_of_turtles[0].forward(100)
            list_of_turtles[1].forward(100)
            list_of_turtles[2].forward(100)
            list_of_turtles[3].forward(100)
            
    
    

    




# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Cierra la ventana al hacer click en la pantalla
screen.exitonclick()
