import turtle
from ru_local import *

def drakon(order, x1, x2, y1, y2):
    if order == 0:
        turtle.up()
        turtle.goto(x1, y1)
        turtle.down()
        turtle.goto(x2, y2)
    else:
        dx = (x2 - x1)/2
        dy = (y2 - y1)/2
        nx = x1 + dx - dy
        ny = y1 + dy + dx
        drakon(order - 1, x2, nx, y2, ny)
        drakon(order - 1, x1, nx, y1, ny)


def main():
    turtle.speed(0)
    n = int(input(GLUB_OF_SIDE))
    a = int(input(LENGHT))
    x1 = - a
    x2 = a
    y1 = 0
    y2 = 0
    drakon(n, x1, x2, y1, y2)
    turtle.mainloop()


if __name__ == "__main__":
    main()
