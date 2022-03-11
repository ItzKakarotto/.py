#DAY 7 & 8 - PYTHON SNAKE GAME
#; ) - GitHub.com/ItzKakarotto 

import turtle as t
import time
from snake import Snake
from food import Food
from score import Score


#Screen Setup
screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Kakarot's Snake Game")
screen.tracer(0)
screen.listen()

snek = Snake()
food = Food()
score = Score()

screen.onkey(key="Up", fun=snek.up)
screen.onkey(key="Down", fun=snek.down)
screen.onkey(key="Left", fun=snek.left)
screen.onkey(key="Right", fun=snek.right)


score_count=0
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snek.move()
    if snek.head.distance(food)<15:
        score_count+=1
        score.update(score_count)
        food.refresh()
        snek.extend()
    
    if snek.head.xcor()>280 or snek.head.ycor()>280 or snek.head.xcor()<-280 or snek.head.ycor()<-280:
        score.game_over()
        is_game_on=False
        
    for block in snek.blocks:
        if block==snek.head:
            pass
        elif snek.head.distance(block) <10:
            is_game_on=False
            score.game_over()


    

screen.exitonclick()
