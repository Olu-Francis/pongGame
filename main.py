import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
ball = Ball()
score = ScoreBoard()
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

init = True
while init:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.change_y_cor()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.change_x_cor()
    if ball.xcor() > 400:
        ball.ball_reset()
        score.l_points()
    if ball.xcor() < -400:
        ball.ball_reset()
        score.r_points()
