from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square") # instead of : self.paddle_turtle = Turtle(shape="square") (now that it's inherited from Turtle class)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.color("white")
        self.goto(self.x, self.y)

    def move_paddle_up(self):
        if self.ycor() < 240:
            new_ycor = self.ycor() + 20
            self.goto(self.x, new_ycor)

    def move_paddle_down(self):
        if self.ycor() > -222:
            new_ycor = self.ycor() - 20
            self.goto(self.x, new_ycor)

    # no need for this now since Paddle inherits from Turtle class, so similar but no "paddle_turtle"
    # def create_user_paddle(self):
    #     self.paddle_turtle = Turtle(shape="square")
    #     self.paddle_turtle.shapesize(stretch_wid=5, stretch_len=1)
    #     self.paddle_turtle.pu()
    #     self.paddle_turtle.color("white")
    #     self.paddle_turtle.goto(self.x, self.y)
