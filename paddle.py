from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 25
        if new_y < 255:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        if new_y > -255:
            self.goto(self.xcor(), new_y)