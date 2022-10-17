from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall and bounce back
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with the right and left paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    elif ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect if the ball goes beyond the left paddle
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

    # Detect if the ball goes beyond the right paddle
    elif ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()