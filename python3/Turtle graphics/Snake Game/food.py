from turtle import Turtle
import random as r

FOOD_WID = 0.70
FOOD_LEN = 0.70
COLOR = "red"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=FOOD_WID, stretch_len=FOOD_LEN)
        self.color(COLOR)
        self.penup()
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        rand_x, rand_y = r.randint(-280, 280), r.randint(-280, 280)
        self.goto(rand_x, rand_y)
