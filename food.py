from turtle import Turtle
from snake import Snake
from random import randint
class Food(Turtle):
   def __init__(self):
       super().__init__()
       self.shape("circle")
       self.color("red")
       self.shapesize(0.5,0.5)
       self.penup()
       rnd_x=randint(-380,380)
       rnd_y=randint(-380,380)
       self.goto(rnd_x,rnd_y)
   def refresh(self):
        rnd_x = randint(-370, 370)
        rnd_y = randint(-370, 370)
        self.goto(rnd_x, rnd_y)


