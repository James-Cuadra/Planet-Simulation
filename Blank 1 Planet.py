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

def Animate(r, theta, dtheta, direction):
    xc = 0
    yc = 0
    turtle.tracer(0)
    theta += dtheta * direction
    x = r*cos(theta) + xc
    y = r*sin(theta) + yc
    position = [x,y]
    return position, theta

def Manager():
    position = [300, -100]
    r, theta, dtheta, bad = Planet(30, position, 'green', 10, 1)
    while True:
        Planet(30, position, 'green', 10, 1)
        bad, bad, dtheta, direction = Planet(30, position, 'green', 10, 1)
        position, theta = Animate(r, theta, dtheta, direction)
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
