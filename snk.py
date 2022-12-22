from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
f=open("highscore.txt","r+")
c=f.read()
f.close()
ecran=Screen()
ecran.setup(height=800,width=800)
ecran.tracer(0)
ecran.bgcolor("black")
ecran.title("Snake")
x=Turtle()
y=Turtle()
z=Turtle()
t=Turtle()
x.penup()
x.color("red")
x.goto(390,390)
x.pendown()
x.hideturtle()
x.right(90)
x.forward(780)
y.penup()
y.color("red")
y.goto(-396,-396)
y.pendown()
y.hideturtle()
y.left(90)
y.forward(780)
z.penup()
z.color("red")
z.goto(390,390)
z.pendown()
z.hideturtle()
z.right(180)
z.forward(780)
t.penup()
t.color("red")
t.goto(-390,-390)
t.pendown()
t.hideturtle()
t.forward(780)
sarpe=Snake()
mancare=Food()
scor=Scoreboard()
scor.highscore=int(c)
game=True
ecran.listen()
ecran.onkey(sarpe.up,"w")
ecran.onkey(sarpe.down,"s")
ecran.onkey(sarpe.left,"a")
ecran.onkey(sarpe.right,"d")
while game==True:
    ecran.update()
    time.sleep(0.12)
    sarpe.move()
    if sarpe.head.distance(mancare)<15:
        mancare.refresh()
        scor.increase_score()
        sarpe.extend()
    if sarpe.head.xcor()>380 or sarpe.head.xcor()<-380 or sarpe.head.ycor()>380 or sarpe.head.ycor()<-380:
        game=False
        if scor.score>int(c):
            g=open("highscore.txt", "w+")
            g.write(str(scor.score))
            g.close()
            scor.game_over_new(scor.score)
        else:
            scor.game_over()
    for x in sarpe.segments:
        if x==sarpe.head:
            pass
        elif sarpe.head.distance(x)<10:
            game = False
            scor.game_over()
ecran.exitonclick()