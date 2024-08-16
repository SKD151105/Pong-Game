# TODO: 1. Create the screen
# TODO: 2. Create and move a paddle
# TODO: 3. Create another paddle
# TODO: 4. Create the ball and make it move
# TODO: 5. Detect collision with wall and bounce
# TODO: 6. Detect collision with paddle
# TODO: 7. Detect when paddle misses
# TODO: 8. Keep score

# This is how you should break a problem first and organise it
# Next you can think of the different classes you can make
# Then start solving bit by bit

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen = Screen()
screen.bgcolor("DarkSlateGray")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with the wall
    if abs(ball.ycor()) >= 290:
        ball.bounce_y()
        # Changes the direction of the ball before it moves next

    # Detecting collision with the paddles
    if (330 <= ball.xcor() <= 340 and ball.distance(right_paddle) < 51 or
            -340 <= ball.xcor() <= -330 and ball.distance(left_paddle) < 51):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
