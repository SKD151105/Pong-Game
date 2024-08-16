from turtle import Turtle
FONT = ("Ariel", 60, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        # Updating the score
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=FONT)
        self.goto(0, 210)
        self.write(":", align="center", font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()
