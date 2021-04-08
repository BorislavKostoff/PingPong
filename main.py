import turtle

wn = turtle.Screen()
wn.title("Ping Pong by BK")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ping Pong Ball
ping_pong = turtle.Turtle()
ping_pong.speed(0)
ping_pong.shape("circle")
ping_pong.color("white")
ping_pong.penup()
ping_pong.goto(0, 0)
ping_pong.dx = 0.2
ping_pong.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ping pong
    ping_pong.setx(ping_pong.xcor() + ping_pong.dx)
    ping_pong.sety(ping_pong.ycor() + ping_pong.dy)

    # Border check
    if ping_pong.ycor() > 290:
        ping_pong.sety(290)
        ping_pong.dy *= -1

    if ping_pong.ycor() < -290:
        ping_pong.sety(-290)
        ping_pong.dy *= -1

    if ping_pong.xcor() > 390:
        ping_pong.goto(0, 0)
        ping_pong.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ping_pong.xcor() < -390:
        ping_pong.goto(0, 0)
        ping_pong.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and Ping Pong collisions
    if (350 > ping_pong.xcor() > 340) and (paddle_b.ycor() + 50 > ping_pong.ycor() > paddle_b.ycor() - 50):
        ping_pong.setx(340)
        ping_pong.dx *= -1

    if (-340 > ping_pong.xcor() > -350) and (paddle_a.ycor() + 50 > ping_pong.ycor() > paddle_a.ycor() - 50):
        ping_pong.setx(-340)
        ping_pong.dx *= -1
