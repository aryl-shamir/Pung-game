"""
Pong Game (or 'Pung' as customized):
A two-player classic paddle game using Turtle graphics.

Controls:
- Right Paddle: Arrow Up and Arrow Down
- Left Paddle: 'w' and 's'
"""

# ---- Import libraries ----
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# ---- Set up screen ----
screen = Screen()
screen.title("Welcome to the Pung game.")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic updates for smooth animation
screen.listen()

# ---- Instantiate game objects ----
left_paddle = Paddle(position=(-370, 0))
right_paddle = Paddle(position=(370, 0))
ball = Ball()
right_score = Scoreboard(position=(30, 260))
left_score = Scoreboard(position=(-30, 260))

# ---- Define key bindings for paddle movement ----
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# ---- Game loop ----
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # ---- Collision with top or bottom wall ----
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # ---- Collision with right paddle ----
    if ball.distance(right_paddle) < 45 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()

    # ---- Collision with left paddle ----
    if ball.distance(left_paddle) < 45 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    # ---- Right paddle misses ----
    if ball.xcor() > 380:
        ball.goto_center()
        left_score.increase_score()

    # ---- Left paddle misses ----
    if ball.xcor() < -380:
        ball.goto_center()
        right_score.increase_score()

# ---- Exit on click ----
screen.exitonclick()
