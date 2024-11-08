from turtle import *
 

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        # with open("data.txt") as data:
        #   self.high_score = int(data.read())
        try:
            with open("data.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write("0")
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial",24,"normal"))    

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="center", font= ("Arial", 24, "normal"))

    def increase_score(self):
        self.score +=1
        self.update_score()
