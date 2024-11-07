from turtle import *
import time
from snake import Snake
from food import Food 
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)            #Screen tracer and screen update together are used to make the snake look like a coherent piece instead of 3 squares moving

snake = Snake ()
food = Food ()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision w food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision w wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -280:
        game_on = False 
        scoreboard.game_over()
    #detect collision w tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

def close_game():
    screen.bye()

screen.listen()
screen.onkey(close_game, "Escape")
#keep the main window open
screen.mainloop()