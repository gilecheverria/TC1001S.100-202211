"""Cannon, hitting targets with projectiles.
Team members
1) Mario Ignacio Frías Piña 
2) Diego Emiliano Figueroa Guillén
3) Santiago Tena Zozaya 

Exercises
1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector
import random

ball = vector(-200,-200)
speed = vector(0, 0)
targets = []
score = 0
colors = ["pink", "orange", "yellow", "blue"]
colorBalls = random.choice(colors)
sp=5 #speed

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x*sp + 200) / 25
        speed.y = (y*sp + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, colorBalls)

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    goto(0,190)
    write(score,font=("Arial",20))
        
    update()

def move():
    global score
    "Move ball and targets."
    # Generate a new target at random times
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move the existing targets
    for target in targets:
        target.x -= 2

    # Move the cannon shot
    if inside(ball):
        speed.y -= 0.35*sp
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target and adds score
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            score += 1
            print("HIT! Score is:{:d}".format(score))

    draw()

    # Detect when a target reaches the left side
    for target in targets:
        if not inside(target):
            target.x = 200
            #targets.remove(target)
            #return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()  

