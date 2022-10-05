from turtle import Turtle, Screen

FONT1 = ('BankGothic Md BT', 17, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("white")
        self.user1_score_number = 0
        self.user2_score_number = 0

    def refresh_scoreboard(self):
        self.clear()
        self.goto(x=-40, y=200)
        self.pd()
        self.write(f"{self.user1_score_number}", font=FONT1, align="center")
        self.pu()
        self.goto(x=40, y=200)
        self.pd()
        self.write(f"{self.user2_score_number}", font=FONT1, align="center")
        self.pu()

    def update_user1_score(self):
        self.user1_score_number += 1
        self.refresh_scoreboard()

    def update_user2_score(self):
        self.user2_score_number += 1
        self.refresh_scoreboard()
