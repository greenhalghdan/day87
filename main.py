import time
from turtle import Screen, Turtle
from paddle import Paddle
from block import Block
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")

screen.tracer(0)

paddle = Paddle((0, -200))
blocks = []
block01 = Block((-200,200), "red")
block04 = Block((-100,200),"red")
block02 = Block((0,200), "red")
block03 = Block((100,200),"red")
block03 = Block((200,200),"red")
block13 = Block((200,180),"orange")
block14 = Block((100,180),"orange")
block15 = Block((-100,180),"orange")
block11 = Block((-200,180), "orange")
block12 = Block((0,180), "orange")
block23 = Block((200,160),"yellow")
block24 = Block((-100,160),"yellow")
block25 = Block((100,160),"yellow")
block21 = Block((-200,160), "yellow")
block22 = Block((0,160), "yellow")
block33 = Block((200,140),"green")
block31 = Block((-200,140), "green")
block34 = Block((-100,140), "green")
block35 = Block((100,140), "green")
block32 = Block((0,140), "green")
block43 = Block((200,120),"blue")
block41 = Block((-200,120), "blue")
block42 = Block((0,120), "blue")
block44 = Block((100,120), "blue")
block45 = Block((-100,120), "blue")

blocks.append(block01)
blocks.append(block02)
blocks.append(block03)
blocks.append(block04)

blocks.append(block11)
blocks.append(block12)
blocks.append(block13)
blocks.append(block14)

blocks.append(block21)
blocks.append(block22)
blocks.append(block23)
blocks.append(block24)

blocks.append(block31)
blocks.append(block32)
blocks.append(block33)
blocks.append(block34)

blocks.append(block41)
blocks.append(block42)
blocks.append(block45)
blocks.append(block44)

ball = Ball()
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")


playing = True

while playing:
    screen.update()
    ball.move_ball()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()
    if ball.xcor() > 220 or ball.xcor() < -220:
        ball.bounce_x()
    for block in blocks:
        w = int(ball.ycor())
        x = int(ball.xcor())
        y = int(block.xcor())
        z = int(block.ycor())
        if w > z - 20 and w < z + 20 and x > y - 50 and x < y + 50:
        #if ball.distance(block) < 50:
            print(f"w: {w}")
            print(f"x: {x}")
            print(f"y: {y}")
            print(f"z = {z}")
            #time.sleep(10)
            ball.bounce_y()
            #block.reset()
            #block.color("white")
            #time.sleep(2)
            block.goto(30000, 3000)
            #time.sleep(2)
    for block in blocks:
        print(block.pos())
    if ball.distance(paddle) < 50:
        ball.bounce_y()
screen.update()
screen.exitonclick()




