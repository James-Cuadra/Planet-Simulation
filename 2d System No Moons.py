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
    return r, theta, dtheta

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
    turtle.tracer(0)
    num = int(input('num of planets '))
    RList = [] #List of orbit distances
    DthetaList = [] #List of dtheta
    ThetaList = [] #List of thetas
    info = [] #List of info
    positionList = [] #List of Positions
    for planet in range(num):
         rawinfo = inpute() #size, pos, colour, yearlength, direction
         info.append(rawinfo)
    print(info)
    for item in info:
        i = info.index(item)
        r, theta, dtheta= Planet(info[i][0],info[i][1],info[i][2],info[i][3],info[i][4])
        RList.append(r)
        DthetaList.append(dtheta)
        ThetaList.append(theta)
        positionList.append(info[i][1])
    while True:
        for item in info:
            i = info.index(item)
            Planet(item[0], positionList[i],item[2],item[3],item[4])
            positionList[i], theta = Animate(RList[i], ThetaList[i], DthetaList[i], item[4])
            ThetaList[i] = theta
            distance = sqrt((abs(positionList[i][0]-0)**2)+(abs(positionList[i][1]-0)**2))
            print(str(distance))
            DrawSun()
        turtle.update()
        time.sleep(0.001)
        turtle.clear()
    '''
    position = [300, -100]
    r, theta, dtheta, bad = Planet(5, position, 'green', 365, 1)
    position2 = [350, -100]
    r2, theta2, dtheta2, bad = Planet(10, position2, 'red', 280, 1)
    while True:
        Planet(5, position, 'green', 365, 1)
        bad, bad, dtheta, direction = Planet(5, position, 'green', 365, 1)
        position, theta = Animate(r, theta, dtheta, direction)
        Planet(10, position2, 'green', 365, -1)
        bad, bad, dtheta2, direction2 = Planet(10, position2, 'red', 280, -1)
        position2, theta2 = Animate(r2, theta2, dtheta2, direction2)
        DrawSun()
        distance1 = sqrt((abs(position[0]-0)**2)+(abs(position[1]-0)**2))
        distance2 = sqrt((abs(position2[0]-0)**2)+(abs(position2[1]-0)**2))
        print(str(distance1), str(distance2))
        turtle.update()
        turtle.clear()
    '''

def DrawSun():
    radius = 100
    position = [0, 0]
    colour = "yellow"
    DrawCircle(radius, position, colour)

Background()
turtle.bgcolor('black')
DrawSun()

def inpute():
    i = int(input('press 1 for list or 2 for interactive or 3 for random '))
    if i == 2:
        size = int(input('size '))
        x = int(input('distance from sun '))
        pos = [x, -50]
        colour = input('colour ')
        yearlength = int(input('yearlength '))
        direction = int(input('direction '))
        return [size, pos, colour, yearlength, direction]
    if i == 2:
        list = input('List: ')
        return list
    if i == 3:
        size = random.randint(3,40)
        y = [50,-50]
        pos = [random.randint(100, 600), random.choice(y)]
        colours = ['green', 'red', 'yellow', 'pink', 'purple', 'orange', 'grey', 'blue', 'green']
        colour = random.choice(colours)
        yearlength = random.randint(1, 100)
        directions = [1,-1]
        direction = random.choice(directions)
        return [size, pos, colour, yearlength, direction]


Manager()
'''
pos = [300, -50]
Planet(5, pos, 'green', 365, 1)
pos = [350, -50]
Planet(10, pos, 'red', 230, -1)
Manager()
turtle.done()
'''
