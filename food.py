from turtle import Turtle
import random


# inheritance concept in use. now food class can use all the methods and the variables(attributes) of Turtle class is available
class Food(Turtle):

    def __init__(self):
        super().__init__()
#         as inheritance is complete I can use the methods and  attributes available
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.random_food()


    def random_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)