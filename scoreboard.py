from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 360)
        self.color("white")
        self.hideturtle()
        self.score=0
        self.highscore=0
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER:You got {self.score} points!", align="center", font=("Arial", 24, "normal"))
        self.goto(0,-100)
        self.write(f"HIGH SCORE: {self.highscore} points!", align="center", font=("Arial", 24, "normal"))
    def game_over_new(self,val):
        self.goto(0,0)
        self.write(f"GAME OVER:You got {self.score} points!", align="center", font=("Arial", 24, "normal"))
        self.goto(0,-100)
        self.write(f"NEW HIGH SCORE: {val} points!", align="center", font=("Arial", 24, "normal"))
