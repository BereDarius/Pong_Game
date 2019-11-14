import turtle
from start_pong import start_game

wnd = turtle.Screen()
wnd.title("Pong")
wnd.bgcolor("black")
wnd.setup(width=1.0, height=1.0)
wnd.tracer(0)

# Menu
menu_items = {
    "start_game": True,
    "exit": False
}

menu_start = turtle.Turtle()
menu_start.speed(0)
menu_start.color("white")
menu_start.penup()
menu_start.hideturtle()
menu_start.goto(0, wnd.window_height() // 4)
menu_start.write("Start game", align="center", font=("Courier", 24, "normal"))

menu_exit = turtle.Turtle()
menu_exit.speed(0)
menu_exit.color("white")
menu_exit.penup()
menu_exit.hideturtle()
menu_exit.goto(0, -wnd.window_height() // 4)
menu_exit.write("Exit", align="center", font=("Courier", 24, "normal"))

# Functions


def next_menu_item():
    if menu_items["start_game"]:
        menu_items["start_game"] = False
        menu_items["exit"] = True
    else:
        menu_items["start_game"] = True
        menu_items["exit"] = False


def previous_menu_item():
    if menu_items["start_game"]:
        menu_items["start_game"] = False
        menu_items["exit"] = True
    else:
        menu_items["start_game"] = True
        menu_items["exit"] = False


def select_menu_item():
    if menu_items["start_game"]:
        wnd.clear()
        start_game()
    elif menu_items["exit"]:
        wnd.bye()


# Key bindings
wnd.listen()
wnd.onkeypress(next_menu_item, 'Up')
wnd.onkeypress(previous_menu_item, 'Down')
wnd.onkeypress(next_menu_item, 'w')
wnd.onkeypress(previous_menu_item, 's')
wnd.onkeypress(select_menu_item, 'Return')


while True:
    wnd.update()
    if menu_items["start_game"]:
        menu_start.clear()
        menu_start.write("Start game", align="center", font=("Courier", 24, "normal", "underline"))
        menu_exit.clear()
        menu_exit.write("Exit", align="center", font=("Courier", 24, "normal"))
    elif menu_items["exit"]:
        menu_exit.clear()
        menu_exit.write("Exit", align="center", font=("Courier", 24, "normal", "underline"))
        menu_start.clear()
        menu_start.write("Start game", align="center", font=("Courier", 24, "normal"))
