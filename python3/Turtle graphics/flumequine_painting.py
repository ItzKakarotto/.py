#DAY 6 - MILLION DOLLARS PAINTING! (refer to https://www.artsy.net/artwork/damien-hirst-flumequine-15)
# ; ) - github.com/ItzKakarotto


from turtle import  Turtle, Screen, colormode
from random import choice, randint
colormode(255)

hirst_color = [(212, 154, 98), (242, 249, 247), (236, 241, 245), (53, 107, 131), (199, 142, 34), (178, 78, 33), (116, 156, 171), (124, 79, 98), (123, 175, 157), (226, 198, 129), (190, 88, 109), (12, 49, 64), (56, 39, 19), (40, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (225, 93, 78), (244, 163, 160), (38, 32, 34), (3, 25, 25), (79, 147, 169), (163, 26, 21), (19, 79, 91), (235, 166, 170), (171, 207, 190), (102, 127, 158), (163, 203, 211), (61, 60, 72), (79, 66, 42), (182, 189, 207), (15, 107, 103)]


sai = Turtle()
sai.speed("fastest")
sai.penup()
sai.hideturtle()

sai.setheading(240)
sai.forward(669)
sai.setheading(0)


def draw_circle():
    """you can use Turtle().dot(20, color but idk why it doesn't render in my device"""
    sai.color(choice(hirst_color))
    sai.begin_fill()
    sai.circle(20)
    sai.end_fill()


for i in range(1, 101):
    draw_circle()
    sai.forward(75)
    if i%10==0:
        sai.setheading(90)
        sai.forward(75)
        sai.setheading(180)
        sai.forward(750)
        sai.setheading(360)



screen = Screen()
screen.exitonclick()
