#DAY 7 - TURTLE RACE GAME
#Requirements - Graphical Interface
#;) - GitHub.com/ItzKakarotto

import turtle as t
import random as r

#Vars
color_list = ["purple", "indigo", "green", "yellow", "orange", "red"]
y_cords = [-100, -60, -20, 20, 60, 100]
turtle_list = []


#Initialization
scr = t.Screen()
scr.setup(width=500, height=400)
your_turtle = scr.textinput(title="Choose Your Turtle", prompt="Which turtle will win the race")
for i in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_cords[i])
    new_turtle.speed("slow")
    turtle_list.append(new_turtle)


#The Code
is_on=True
while is_on:
    for i in range(6):
        turtle = turtle_list[i]
        if turtle.xcor()>235:
            is_on=False
            clr = turtle.color()[0].lower()
            if your_turtle.lower()==clr:
                print(f"You won {clr} reached first")
            else:
                print(f"You lost {clr} reached first")
        
        move = r.randint(0, 8)
        turtle.forward(move)


scr.exitonclick()
