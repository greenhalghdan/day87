from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(
            stretch_wid=1,
            stretch_len=5
        )
        self.color("white")
        self.speed("fastest")
        self.goto(pos)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(x=new_x,y=-200)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(x=new_x,y=-200)