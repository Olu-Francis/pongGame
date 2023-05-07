from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_x_cor = 10
        self.ball_y_cor = 10
        self.shape('circle')
        self.penup()
        self.color('white')
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.ball_x_cor
        new_y = self.ycor() + self.ball_y_cor
        self.goto(new_x, new_y)

    def change_y_cor(self):
        self.ball_y_cor *= -1

    def change_x_cor(self):
        self.ball_x_cor *= -1
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.home()
        self.ball_speed = 0.1
        self.change_x_cor()
