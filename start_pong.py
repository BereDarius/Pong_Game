import turtle
import os
import winsound
import sys


def start_game():
    # Screen setup
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=1.0, height=1.0)
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
    paddle_a.goto(-wn.window_width() // 2.5, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(wn.window_width() // 2.5, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1

    # Border drawing
    border = turtle.Turtle()
    border.speed(0)
    border.color("white")
    border.pensize(5)
    border.penup()
    border.goto(-wn.window_width() // 2.3 - 9, wn.window_height() // 2.5 - 2)
    border.pendown()
    border.goto(wn.window_width() // 2.3 + 9, wn.window_height() // 2.5 - 2)
    border.goto(wn.window_width() // 2.3 + 9, -wn.window_height() // 2.5 + 2)
    border.goto(-wn.window_width() // 2.3 - 9, -wn.window_height() // 2.5 + 2)
    border.goto(-wn.window_width() // 2.3 - 9, wn.window_height() // 2.5 - 2)
    border.penup()
    border.hideturtle()

    # Score board
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.color("white")
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, wn.window_height() // 2.4)
    score_board.write("Player A: 0  Player B: 0",
                      align="center",
                      font=("Courier", 24, "normal"))

    # Function

    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        if not (paddle_a.ycor() + 60 > wn.window_height() // 2.5 - 2):
            paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        if not (paddle_a.ycor() - 60 < -wn.window_height() // 2.5 + 2):
            paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        if not (paddle_b.ycor() + 60 > wn.window_height() // 2.5 - 2):
            paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        if not (paddle_b.ycor() - 60 < -wn.window_height() // 2.5 + 2):
            paddle_b.sety(y)

    def goodbye():
        wn.bye()

    def ball_speed_reset():
        ball.dx = 1
        ball.dy = 1

    def ball_speed_up():
        if (ball.dx < 0):
            ball.dx -= 0.3
        if (ball.dx > 0):
            ball.dx += 0.3
        if (ball.dy < 0):
            ball.dy -= 0.3
        if (ball.dy > 0):
            ball.dy += 0.3

    # Keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, 'w')
    wn.onkeypress(paddle_a_down, 's')
    wn.onkeypress(paddle_b_up, 'Up')
    wn.onkeypress(paddle_b_down, 'Down')
    wn.onkeypress(goodbye, 'Escape')

    # Main game loop
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > wn.window_height() // 2.5:
            ball.sety(wn.window_height() // 2.5)
            ball.dy *= -1
            if sys.platform == "win32" or sys.platform == "cygwin":
                winsound.PlaySound(
                    "pong_blip", winsound.SND_ASYNC | winsound.SND_FILENAME)
            elif sys.platform == "darwin":
                os.system("afplay pong_blip.wav&")
            else:
                os.system("aplay pong_blip.wav&")

        if ball.ycor() < -wn.window_height() // 2.5:
            ball.sety(-wn.window_height() // 2.5)
            ball.dy *= -1
            if sys.platform == "win32" or sys.platform == "cygwin":
                winsound.PlaySound(
                    "pong_blip", winsound.SND_ASYNC | winsound.SND_FILENAME)
            elif sys.platform == "darwin":
                os.system("afplay pong_blip.wav&")
            else:
                os.system("aplay pong_blip.wav&")

        if ball.xcor() > wn.window_width() // 2.3:
            ball.goto(0, 0)
            ball_speed_reset()
            ball.dx *= -1
            score_a += 1
            score_board.clear()
            score_board.write("Player A: {}  Player B: {}".format(score_a, score_b),
                              align="center",
                              font=("Courier", 24, "normal"))

        if ball.xcor() < -wn.window_width() // 2.3:
            ball.goto(0, 0)
            ball_speed_reset()
            ball.dx *= -1
            score_b += 1
            score_board.clear()
            score_board.write("Player A: {}  Player B: {}".format(score_a, score_b),
                              align="center",
                              font=("Courier", 24, "normal"))

        # Paddle and ball collisions
        if (
            ball.xcor() > paddle_b.xcor() - 20 and
            ball.xcor() < paddle_b.xcor() + 2 and
            ball.ycor() < paddle_b.ycor() + 40 and
            ball.ycor() > paddle_b.ycor() - 40
        ):
            ball.setx(paddle_b.xcor() - 20)
            ball.dx *= -1
            ball_speed_up()
            if sys.platform == "win32" or sys.platform == "cygwin":
                winsound.PlaySound(
                    "pong_blip", winsound.SND_ASYNC | winsound.SND_FILENAME)
            elif sys.platform == "darwin":
                os.system("afplay pong_blip.wav&")
            else:
                os.system("aplay pong_blip.wav&")

        if (
            ball.xcor() < paddle_a.xcor() + 20 and
            ball.xcor() > paddle_a.xcor() - 2 and
            ball.ycor() < paddle_a.ycor() + 40 and
            ball.ycor() > paddle_a.ycor() - 40
        ):
            ball.setx(paddle_a.xcor() + 20)
            ball.dx *= -1
            ball_speed_up()
            if sys.platform == "win32" or sys.platform == "cygwin":
                winsound.PlaySound(
                    "pong_blip", winsound.SND_ASYNC | winsound.SND_FILENAME)
            elif sys.platform == "darwin":
                os.system("afplay pong_blip.wav&")
            else:
                os.system("aplay pong_blip.wav&")
