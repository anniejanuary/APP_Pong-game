from turtle import Turtle, Screen
from score import ScoreBoard
import random
import time

screen = Screen()
score = ScoreBoard()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.showturtle()
        self.pu()
        self.color("yellow")
        self.x_forward = 10
        self.y_forward = 10
        self.ball_speed = 0.06

    def first_ball_direction(self):
        self.setheading(random.randint(*random.choice([(120, 140), (220, 240)])))

    def wall_collision(self, keep_ballin, user1_paddle, user2_paddle):
        if self.ycor() >= 280 or self.ycor() <= -265:
            self.y_forward *= -1

    def paddle_collision(self, keep_ballin, user1_paddle, score, user2_paddle):
        if user1_paddle.distance(self) < 55 and self.xcor() < -350:
            score.update_user1_score()
            self.x_forward *= -1
            self.increase_ball_speed()
        if user2_paddle.distance(self) < 55 and self.xcor() > 352:
            score.update_user2_score()
            self.x_forward *= -1
            self.increase_ball_speed()

    def ball_move(self, keep_ballin, user1_paddle, user2_paddle):
        while keep_ballin:
            time.sleep(self.ball_speed)
            next_x = self.xcor() + self.x_forward
            next_y = self.ycor() + self.y_forward
            self.goto(next_x, next_y)
            screen.update()
            self.wall_collision(keep_ballin, user1_paddle, user2_paddle)
            self.paddle_collision(keep_ballin, user1_paddle, score, user2_paddle)
            if self.xcor() < -380 or self.xcor() > 380:
                self.miss_and_reset(keep_ballin, user1_paddle, user2_paddle)
            screen.listen()
            screen.onkeypress(user1_paddle.move_paddle_up, "w")
            screen.onkeypress(user1_paddle.move_paddle_down, "s")
            screen.onkeypress(user2_paddle.move_paddle_up, "Up")
            screen.onkeypress(user2_paddle.move_paddle_down, "Down")

    def miss_and_reset (self, keep_ballin, user1_paddle, user2_paddle):
        if self.xcor() < -360:
            score.update_user2_score()
        if self.xcor() > 362:
            score.update_user1_score()
        self.goto(0, 0)
        self.ball_speed = 0.06
        self.x_forward *= -1

    def increase_ball_speed(self):
        self.ball_speed *= 0.9
        time.sleep(self.ball_speed)

# WALL COLLISION, unnecessarily complicated:
    #if self.ycor() >= 282 or self.ycor() <= -265:
        #current_heading = self.heading()
        # current_heading = 360 - current_heading
        # self.setheading(current_heading)
        #self.ball_move(keep_ballin, user1_paddle, user2_paddle)

#PADDLES COLLISION
   # unnecessarily complicated for: if user1_paddle.distance(self) < 50 and self.xcor() < -350:
    # if current_heading in range(91, 179):   # II quadrant
    #     current_heading = 180 - current_heading
    # if ball comes from the right in a downwards direction
    # if current_heading in range(181, 269):   # III quadrant
    #     current_heading = 270 + (270 - current_heading)

    # unnecessarily complicated for:   if user2_paddle.distance(self) < 50 and self.xcor() > 355:
    # if current_heading in range(1, 89):   # I quadrant
    #     current_heading += (90 - current_heading) *2
    # if ball comes from the left in an downwards direction
    # if current_heading in range(271, 359):  # IV quadrant
    #     current_heading -= (current_heading - 270) *2
