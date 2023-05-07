from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)
