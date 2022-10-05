from turtle import Screen
from board import Board
from score import ScoreBoard
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
board = Board()
screen.update()
ball = Ball()
score_board = ScoreBoard()
user1_paddle = Paddle(x=-380, y=0)
user2_paddle = Paddle(x=380, y=0)
screen.update()

keep_ballin = True
ball.first_ball_direction()

while keep_ballin:
    screen.update()
    ball.ball_move(keep_ballin, user1_paddle, user2_paddle)

screen.exitonclick()
