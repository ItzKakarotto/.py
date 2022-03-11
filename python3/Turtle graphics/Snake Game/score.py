from turtle import Turtle

FONT = ('Courier', 18, 'normal')
FONTGO = ('Courier', 28, 'normal')
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.update(0)
        
    def update(self, score):
        self.score_count=score
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {self.score_count}", move=False, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONTGO)
        
