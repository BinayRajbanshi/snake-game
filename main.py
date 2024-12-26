import random
import turtle as t
import time

from snake import Snake
from food import Food
from score import Score
from border import  Border

screen = t.Screen()
screen.title("My snake game")
screen.screensize(600, 600)
screen.bgcolor("black")
border = Border()
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()
# food.random_food()



screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # comparing the distance between the head of the snake and the food to detect the collision between the food and the snake head
    if snake.segments[0].distance(food) < 15:
        snake.extend_segment()
        score.score_increase()
        food.random_food()

#     detecting the collision with the walls
    if (snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290
            or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290):
        score.reset_score()
        snake.reset()

#     DETECTING colllisions with the snake body
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass # initially i thought it was return. but it is pass instead
        elif snake.segments[0].distance(segment) < 5 :
            score.reset_score()
            snake.reset()


screen.exitonclick()