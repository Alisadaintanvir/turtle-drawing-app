from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()

screen.onkeypress(lambda: timmy.forward(10), "d")
screen.onkeypress(lambda: timmy.backward(10), "a")
screen.onkeypress(lambda: timmy.left(10), "w")
screen.onkeypress(lambda: timmy.right(10), "s")

screen.listen()
screen.exitonclick()
