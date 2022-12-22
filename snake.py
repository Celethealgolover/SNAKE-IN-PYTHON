from turtle import Turtle
START_POS=[(0,0),(-20,0),(-40,0)]
MOV_DIS=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for x in START_POS:
            self.add_segment(x)
    def add_segment(self,position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOV_DIS)
    def up(self):
        if self.head.heading()!=270:
          self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
          self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:
          self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:
          self.head.setheading(0)
