from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)


def move_back():
    tim.back(10)


def tilt_right():
    tim.right(10)


def tilt_left():
    tim.left(10)

def clear():
    # tim.penup()
    # tim.home()
    # tim.pendown()
    # screen.reset()
    screen.reset() #both work fine




screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="d", fun=tilt_right)
screen.onkeypress(key="a", fun=tilt_left)
screen.onkeypress(key="c", fun=clear)


screen.exitonclick()