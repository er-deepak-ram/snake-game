from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()
