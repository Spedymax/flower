import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen = turtle.Screen()
screen.bgcolor("black")
t.color("pink")
t.speed(0)


def corazon(k):
    return 16 * math.sin(k) ** 3


def corazon1(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


t.penup()
t.goto(corazon(1) * 18, corazon1(1) * 18)
t.pendown()

for i in range(600):
    t.goto(corazon(i) * 18, corazon1(i) * 18)
    for j in range(5):
        t.color("pink")

t.color("gold")
t.penup()
t.goto(115, -40)
t.pendown()
t.write("I LOVE YOU!", False, "right", ("arial", 30, "bold"))

t.hideturtle()
turtle.done()
