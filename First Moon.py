import turtle
from math import *
import random
import time

screen = turtle.Screen()
screen.setup(960,800)
turtle.delay(0)
turtle.speed(0)
turtle.colormode(255)
turtle.ht()
background_turtle = turtle.Turtle()
background_turtle.ht()
background_turtle.speed(0)

def Background():
    background_turtle.color(255,255,102)
    background_turtle.penup()
    background_turtle.goto(-1000, 1000)
    for z in range(0,500):
        background_turtle.pendown()
        background_turtle.begin_fill()
        for i in range(5):
            background_turtle.forward(5)
            background_turtle.right(144)
        background_turtle.end_fill()
        background_turtle.penup()
        background_turtle.setx(random.randint(-1000,1000))
        background_turtle.sety(random.randint(-1000, 1000))

def DrawCircle(radius, position, colour):
    turtle.color(colour)
    turtle.penup()
    turtle.goto(position[0],position[1])
    turtle.pendown()
    turtle.dot(radius*2, colour)

def Planet(radius, position, colour, orbittime, direction):
    dtheta = (2 * pi) / (orbittime*100)
    r = abs(position[0]-0)
    theta = 0
    DrawCircle(radius, position, colour)
    return r, theta, dtheta, direction

def Moon(radius, moonpos, colour, orbittimemoon, direction, FatherPos, r):
    dtheta = (2 * pi) / (orbittimemoon*100)
    theta = 0
    DrawCircle(radius, moonpos, colour)
    return r, theta, dtheta, direction

def Animate(r, theta, dtheta, direction, c):
    print(type(c))
    xc = c[0]
    xy = c[1]
    turtle.tracer(0)
    theta += dtheta * direction
    x = r*cos(theta) + xc
    y = r*sin(theta) + xy
    position = [x,y]
    return position, theta

def Manager():
    planet = [0, 0]
    position = [300, -100]
    moonpos = [300, -150]
    moonpos2 = [300, -150]
    r, theta, dtheta, bad = Planet(30, position, 'blue', 10, 1)
    r2, theta2, dtheta2, bad = Moon(10, moonpos, 'grey', 6, -1, position, 100)
    r3, theta3, dtheta3, bad = Moon(10, moonpos2, 'grey', 6, 1, position, 50)
    while True:
        Planet(30, position, 'green', 12, 1)
        Moon(10, moonpos, 'blue', 6, -1, position, 100)
        Moon(10, moonpos2, 'grey', 6, 1, position, 50)
        print(str(moonpos))
        bad, bad, dtheta, direction = Planet(30, position, 'blue', 12, 1)
        bad, bad, dtheta2, direction2 = Moon(10, moonpos, 'grey', 6, -1, position, 100)
        bad, bad, dtheta3, direction3 = Moon(10, moonpos2, 'grey', 6, 1, position, 50)
        position, theta = Animate(r, theta, dtheta, direction, planet)
        moonpos, theta2 = Animate(r2, theta2, dtheta2, direction2, position)
        moonpos2, theta3 = Animate(r3, theta3, dtheta3, direction3, position)
        print(r2, theta2, dtheta2, direction2)
        DrawSun()
        turtle.update()
        turtle.clear()

def DrawSun():
    radius = 100
    position = [0, 0]
    colour = "yellow"
    DrawCircle(radius, position, colour)

turtle.bgcolor('black')
Background()
DrawSun()

Manager()
