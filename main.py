import time
from turtle import Screen, Turtle
from paddle import Paddle
from block import Block
from ball import Ball

def user_alert(message):
    ALIGNMENT = "center"
    FONT = ("times new roman", 24, "normal")
    alert = Turtle()
    alert.hideturtle()
    alert.color("white")
    alert.write(message, align=ALIGNMENT, font=FONT)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")

screen.tracer(0)

paddle = Paddle((0, -200))
blocks = []
block01 = Block((-200,200), "red")
block02 = Block((0,200), "red")
block03 = Block((100,200),"red")
block04 = Block((-100,200),"red")
block05 = Block((200,200),"red")

block11 = Block((-200,180), "orange")
block12 = Block((0,180), "orange")
block13 = Block((200,180),"orange")
block14 = Block((100,180),"orange")
block15 = Block((-100,180),"orange")

block21 = Block((-200,160), "yellow")
block22 = Block((0,160), "yellow")
block23 = Block((200,160),"yellow")
block24 = Block((-100,160),"yellow")
block25 = Block((100,160),"yellow")

block31 = Block((-200,140), "green")
block32 = Block((0,140), "green")
block33 = Block((200,140),"green")
block34 = Block((-100,140), "green")
block35 = Block((100,140), "green")

block41 = Block((-200,120), "blue")
block42 = Block((0,120), "blue")
block43 = Block((200,120),"blue")
block44 = Block((100,120), "blue")
block45 = Block((-100,120), "blue")

blocks.append(block01)
blocks.append(block02)
blocks.append(block03)
blocks.append(block04)
blocks.append(block05)

blocks.append(block11)
blocks.append(block12)
blocks.append(block13)
blocks.append(block14)
blocks.append(block15)

blocks.append(block21)
blocks.append(block22)
blocks.append(block23)
blocks.append(block24)
blocks.append(block25)

blocks.append(block31)
blocks.append(block32)
blocks.append(block33)
blocks.append(block34)
blocks.append(block35)

blocks.append(block41)
blocks.append(block42)
blocks.append(block43)
blocks.append(block44)
blocks.append(block45)

ball = Ball()
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")


playing = True

while playing:
    time.sleep(0.01)
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
            ball.bounce_y()
            block.goto(30000, 3000)
            blocks.remove(block)
            block._hidden_from_screen = True
    if ball.distance(paddle) < 50:
        ball.bounce_y()
    if len(blocks) <= 0:
        user_alert(message="You Win")
        playing = False
    if int(ball.ycor()) < -249:
        user_alert(message="You Lose")
        playing = False

screen.update()
screen.exitonclick()




