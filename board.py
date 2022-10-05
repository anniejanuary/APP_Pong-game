from turtle import Turtle, Screen
screen = Screen()


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(x=0, y=280)
        self.setheading(270)
        self.pensize(1)

        screen.tracer(0)
        for i in range(28):
            self.pd()
            self.forward(10)
            self.pu()
            self.forward(10)
        self.goto(x=380, y=290)
        self.setheading(180)
        self.pensize(2)
        self.pd()
        self.goto(x=-380, y=290)
        self.pu()
        self.goto(x=-380, y=-280)
        self.pd()
        self.goto(x=380, y=-280)
