import turtle
from ru_local import *

def k(d, n):
    """ Square """
    if n == 0:
        return
    for _ in range(4):
        turtle.forward(d)
        turtle.right(90)
    turtle.up()
    turtle.right(20)
    turtle.forward(d / 4)
    turtle.down()
    return k(0.9 * d, n - 1)


def l(d, n):
    """ Binary tree """
    if n == 0:
        return
    turtle.forward(d)
    turtle.right(30)
    l(d / 2, n - 1)
    turtle.left(60)
    l(d / 2, n - 1)
    turtle.right(30)
    turtle.backward(d)


def branch(n, size):
    """ Fractal 'Branch' """
    if n == 0:
        turtle.left(180)
        return
    x = size/(n+1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.right(135)
    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)


def koch(order, size):
    """ Curve Koch """
    if order == 0:
        turtle.forward(size)
    else:
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)


def snowflake_koch(order, size):
    """ Koch's snowflake"""
    koch(order - 1, size)
    turtle.right(120)
    koch(order - 1, size)
    turtle.right(120)
    koch(order - 1, size)


def mink(order, size):
    """ Minkowski curve """
    if order == 0:
        turtle.forward(size)
    else:
        mink(order-1, size/4)
        turtle.left(90)
        mink(order-1, size/4)
        turtle.right(90)
        mink(order-1, size/4)
        turtle.right(90)
        mink(order-1, size / 4)
        mink(order - 1, size / 4)
        turtle.left(90)
        mink(order - 1, size / 4)
        turtle.left(90)
        mink(order - 1, size / 4)
        turtle.right(90)
        mink(order - 1, size / 4)


def ice(d, n):
    """ Ice fractal #1 """
    if n == 0:
        turtle.forward(d)
    else:
        ice(d/2, n-1)
        turtle.left(90)
        ice(d/4, n-1)
        turtle.right(180)
        ice(d/4, n-1)
        turtle.left(90)
        ice(d/2, n-1)


def ice_snowflake(d, n):
    """ Ice fractal #2 """
    if n == 0:
        turtle.forward(d)
    else:
        ice_snowflake(d/2, n-1)
        turtle.left(120)
        ice_snowflake(d/4, n-1)
        turtle.left(180)
        ice_snowflake(d/4, n-1)
        turtle.left(120)
        ice_snowflake(d/4, n-1)
        turtle.left(180)
        ice_snowflake(d/4, n-1)
        turtle.left(120)
        ice_snowflake(d/2, n-1)


def snowflake(d, n):
    """ Ice fractal snowflake """
    ice_snowflake(d, n-1)
    turtle.right(120)
    ice_snowflake(d, n-1)
    turtle.right(120)
    ice_snowflake(d, n-1)
    turtle.left(180)
    ice_snowflake(d, n-1)
    turtle.left(120)
    ice_snowflake(d, n-1)
    turtle.left(120)
    ice_snowflake(d, n-1)


def levi(n, d):
    """ Levi Curve"""
    if n == 0:
        turtle.forward(d)
    else:
        turtle.left(45)
        levi(n - 1, d)
        turtle.right(90)
        levi(n-1, d)
        turtle.left(45)


def main():
    print(QUEST)
    print(CHOOSE)
    print(NUM_1)
    print(NUM_2)
    print(NUM_3)
    print(NUM_4)
    print(NUM_5)
    print(NUM_6)
    print(NUM_7)
    print(NUM_8)
    print(NUM_9)
    print(NUM_10)
    print(NUM_11)

    m = int(input(INPUT))
    n = int(input(GLUB_OF_SIDE))
    a = int(input(LENGHT))
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    turtle.speed(0)

    if m == 1:
        k(a, n)
    elif m == 2:
        turtle.left(90)
        l(a, n)
    elif m == 3:
        turtle.left(90)
        branch(n, a)
    elif m == 4:
        koch(n, a * 10)
    elif m == 5:
        snowflake_koch(n, a * 3)
    elif m == 6:
        mink(n, a * 50)
    elif m == 7:
        ice(a * 10, n)
    elif m == 8:
        ice_snowflake(a * 10, n)
    elif m == 9:
        snowflake(a, n)
    elif m == 10:
        levi(n, a / 5)
    elif m == 11:
        pass
    turtle.mainloop()


if __name__ == "__main__":
    main()
