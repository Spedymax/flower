import turtle
import random


# Функция для рисования цветка на ветке с увеличенным размером
def draw_flower():
    turtle.color("pink")
    for _ in range(3):  # Рисуем треугольник (цветок)
        turtle.forward(15)  # Увеличиваем размер цветка
        turtle.left(120)
    turtle.color("green")


# Функция для рисования ветви дерева
def draw_branch(length, level):
    if level == 0:
        # На конце ветки рисуем цветок
        turtle.color("green")  # Стебель остаётся зелёным
        draw_flower()
        return

    # Рисуем ветви
    turtle.color("green")
    turtle.forward(length)
    turtle.left(30)
    draw_branch(length * 0.7, level - 1)

    turtle.right(60)
    draw_branch(length * 0.7, level - 1)

    turtle.left(30)
    turtle.backward(length)


# Функция для настройки turtle
def setup_turtle():
    turtle.bgcolor("black")
    turtle.speed(0)  # Умеренная скорость рисования для наблюдения процесса
    turtle.pensize(2)  # Толщина основной ветви
    turtle.color("green")
    turtle.left(90)  # Поворот, чтобы дерево росло вверх
    turtle.up()
    turtle.backward(300)  # Начальная позиция внизу
    turtle.down()


# Основная программа для рисования дерева
def draw_tree(levels):
    setup_turtle()
    draw_branch(150, levels)


# Запрос количества уровней у пользователя
levels = int(input("Насколько сильно вы любите Максимку? (От 1 до 8): "))
while levels > 8 or levels < 1:
    levels = int(input("Введи число от 1 до 8: "))
screen = turtle.Screen()
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

# Рисуем дерево
draw_tree(levels)

# Add a loving message
turtle.penup()
turtle.goto(0, -320)
turtle.color("White")
turtle.write(f"И я тебя люблю!", align="center", font=("Arial", 16, "bold"))

turtle.hideturtle()
# Add these lines to bring the window to the front

turtle.done()
