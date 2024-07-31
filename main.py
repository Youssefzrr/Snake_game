import turtle
import time
from snake import Snake
import random
from food import Food
from score_board import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')

screen.tracer(0)
snake=Snake()
food=Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_on = True
while game_on:
    screen.update()
    snake.move_snake()
    time.sleep(0.1)
    if snake.head.distance(food)<15:
        food.move_to()
        snake.create_segment(snake.segments[-1].position())
        score_board.score_refresh()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game_on = False
            score_board.game_over()

    if any(abs(cord)>280 for cord in (snake.head.xcor(),snake.head.ycor())):
        game_on=False
        score_board.game_over()



screen.exitonclick()
