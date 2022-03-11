import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_blocks(position)
        
    def add_blocks(self, position):
        new_block = t.Turtle(shape="square", visible=False)
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        new_block.showturtle()
        self.blocks.append(new_block)
    
    def extend(self):
        self.add_blocks(self.blocks[-1].position())
        
    def move(self):
        for block_num in range(len(self.blocks)-1, 0, -1):
            x_cor, y_cor = self.blocks[block_num-1].xcor(), self.blocks[block_num-1].ycor()
            self.blocks[block_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)
   
    def up(self):
        if not self.head.heading()==DOWN:
           self.head.setheading(UP)
   
    def down(self):
        if not self.head.heading()==UP:
           self.head.setheading(DOWN)
              
    def left(self):
        if not self.head.heading()==RIGHT:
           self.head.setheading(LEFT)
             
    def right(self):
        if not self.head.heading()==LEFT:
           self.head.setheading(RIGHT)
