from turtle import Turtle
ALIGNMENT = ("center")
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.clear()
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
