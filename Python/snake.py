from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors  = ["green","blue","orange","purple","pink","yellow"] 
colorSnake = random.choice(colors)
colorFood= random.choice(colors)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Move food one step in a random direction"
    direction = randrange(1, 4)
    if direction == 1:
        food.x = food.x - 10
        if not inside(food):
            food.x = food.x + 10
    elif direction == 2:
        food.x = food.x + 10
        if not inside(food):
            food.x = food.x - 10
    elif direction == 3:
        food.y = food.y - 10
        if not inside(food):
            food.y = food.y + 10
    elif direction == 4:
        food.y = food.y + 10
        if not inside(food):
            food.y = food.y - 10
    ontimer(move_food, 2000)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(20, 0), 'Right')
onkey(lambda: change(-20, 0), 'Left')
onkey(lambda: change(0, 20), 'Up')
onkey(lambda: change(0, -20), 'Down')
move()
move_food()
done()
