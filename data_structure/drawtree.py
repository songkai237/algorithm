import turtle


def tree(b, t):
    if b > 5:
        t.forward(b)
        t.right(20)
        tree(b - 15, t)
        t.left(40)
        tree(b - 15, t)
        t.right(20)
        t.backward(b)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    myWin.exitonclick()


main()
