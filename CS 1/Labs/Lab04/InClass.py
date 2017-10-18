from math import *
import turtle as t

""" Init. Conditions: None Needed
    Final Conditions: Turtle speed set, pen up

    Parameters: speed: default value = 0, the speed to set the turtle

    Returns: Nothing

    Description: Initial setup for the turtle
"""
def initialize (speed = 0, width = 10):
    t.speed(speed)
    t.up()
    t.lt(90)
    t.ht()
    t.width(width)

""" Init. Conditions: Center of where you want the figure drawn
    Final Conditions: Pen up, back where you started, initial orientation

    Parameters: n: number of sides that the polygon has (if less than three, does nothing
                r: radius of the circle and the inscribed polygon

    Returns: the perimeter of the drawn polygon

    Description: Draws an "n" sided polygon inscribed in a circle of radius r
"""
def inscribedPolygon(n, r):
    if n >= 3:
        #Initial Positioning
        t.up()
        t.fd(r)
        t.lt(90)
        t.color(0,0,0)

        #draw circle
        t.down()
        t.circle(r)

        #calculate polygon Parameters
        sideLength = (2* r**2 - 2*r**2 * cos(2 * pi / n))**.5
        exteriorAngle = 360/n
        t.color(getColor(n))

        #draw the polygon
        t.lt(exteriorAngle/2)
        i=0
        while i<n-1:
            t.fd(sideLength)
            t.lt(exteriorAngle)
            i += 1
        t.fd(sideLength)

        #go home
        t.up()
        t.rt(90-exteriorAngle/2)
        t.bk(r)
        t.color(0,0,0)

        return sideLength*n
    else:
        print("*****Error*****\nA polygon must have at least 3 sides\nYou entered ", n, "*****Error*****")

def getColor(which):
    which = abs(int(which + .5)) % 3 + 1
    if which == 1:
        return 0, 204/255, 0
    elif which == 2:
        return 0, 0, 1
    else:
        return .4, .5, 1

def totalInscription(n, r, accum = 0):
    if n<3:
        return accum
    else:
        sumSides = inscribedPolygon(n, r)
        return totalInscription(n-1, (r**2 - (sumSides/n)**2/4)**.5,
                         accum + sumSides)

def main():
    t.tracer(0,0)
    initialize(0, 2)
    n = abs(int(int(input("Chose a number of sides (input 0 to exit):")) + .5))
    while n !=0:
        print(totalInscription(n, 275))
        t.update()
        t.clear()
        n = abs(int(int(input("Chose a number of sides (input 0 to exit):")) + .5))


main()