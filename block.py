from turtle import Turtle


class Block(Turtle):
    def __init__(self, pos, colour):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(
            stretch_wid=1,
            stretch_len=5
        )
        self.color(colour)
        self.speed("fastest")
        self.goto(pos)

