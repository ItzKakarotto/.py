from turtle import  Turtle, Screen, colormode
from random import choice, randint

hirst_color = [(212, 154, 98), (242, 249, 247), (236, 241, 245), (53, 107, 131), (199, 142, 34), (178, 78, 33), (116, 156, 171), (124, 79, 98), (123, 175, 157), (226, 198, 129), (190, 88, 109), (12, 49, 64), (56, 39, 19), (40, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (225, 93, 78), (244, 163, 160), (38, 32, 34), (3, 25, 25), (79, 147, 169), (163, 26, 21), (19, 79, 91), (235, 166, 170), (171, 207, 190), (102, 127, 158), (163, 203, 211), (61, 60, 72), (79, 66, 42), (182, 189, 207), (15, 107, 103)]

shapes = [2, 3, 4, 5, 6, 7, 8]
move = ["forward", "left", "backward", "right"]

sai = Turtle()

colormode(255)
sai.shape("turtle")
sai.speed(50)


def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def drawshape(shape):
    for i in range(shape):
        sai.forward(100)
        sai.left(360/shape)
        

def moverandom():
    sai.color(colors())
    ch = choice(move)
    if ch=="forward":
        sai.forward(25)
    if ch=="backward":
        sai.backward(25)
    if ch=="left":
        sai.left(90)
        sai.forward(25)
    if ch=="right":
        sai.right(90)
        sai.forward(25)
 
def draw_sperellogram(radis):
    sai.circle(radis)
    while True:
         sai.color(colors())
         sai.left(10)
         draw_sperellogram(radis)
      
def draw_circle(colour):
    sai.color(colour)
    sai.begin_fill()
    sai.circle(12)
    sai.end_fill()



screen = Screen()
screen.exitonclick()
