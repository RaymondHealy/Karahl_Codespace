import turtle as t
from random import *
from math import *

"""------------------------------------<Constants>------------------------------------"""

"""Defines the absolute value of the max and min of the pond bounding box"""
def kPondSize():
    return 250


"""Defines the minimum random radius of the raindrops"""
def kMinRadius():
    return 5


"""Defines the maximum random radius of the raindrops"""
def kMaxRadius():
    return 25
"""-----------------------------------------------------------------------------------"""


"""---------------------------------<Setup Functions>---------------------------------"""

"""Init. Conditions: None needed
   Final Conditions: Same location, pen up, speed set to the passed parameter
   
   Parameters:  speed: Default 0, passed through to the turtle ".speed()" function
   
   Description: Sets the turtle cursor to its default state (a passed in speed, pen up, color black, fill color black)
"""
def turtleInit(speed=0):
    t.speed(speed)
    t.up()
    t.color("#000000")
    t.fillcolor("#000000")


""" Init. Conditions: Default position (center), pen up, black color
    Final Conditions: Initial position, black pen, pen up, center of a light blue (#ADD8E6) pond
    
    Description: Draws the bounding box for the pond and fills it with a light blue (#ADD8E6) color
"""
def pondInit():
    """Change fill color"""
    t.fillcolor("#add8e6")

    """Move to the bottom of the box"""
    t.rt(90)
    t.fd(kPondSize())
    t.lt(90)

    """Lower pen, draw box, and color it in"""
    t.begin_fill()
    t.down()
    t.fd(kPondSize())
    t.lt(90)
    t.fd(kPondSize() * 2 + 1)
    t.lt(90)
    t.fd(kPondSize() * 2 + 1)
    t.lt(90)
    t.fd(kPondSize() * 2 + 1)
    t.lt(90)
    t.fd(kPondSize() + 1)  # return to initial position
    t.end_fill()
    t.up()

    """Return to initial position & state"""
    t.lt(90)
    t.fd(kPondSize() + 1)
    t.color("#000000")
    t.fillcolor("#000000")
    t.rt(90)
"""-----------------------------------------------------------------------------------"""

"""--------------------------------<Raindrop Functions>-------------------------------"""
""" Init. Conditions: Start from the center of the pond. pointing East
    Final Conditions: Back where you started, same orientation, pen up, black fill and pen colors
    
    Parameters: radius: Radius of the circle to be drawn
                x: x displacement from the origin in pixels
                y: y displacement from the origin in pixels

    Description: Draws a rain drop of the specified radius at displacement (X,Y) from the origin with a random color
"""
def drawRaindrop(radius, x, y):
    print("Radius: ", radius, "\nX: ", x, "\nY: ", y)
    if not (radius + abs(x) <= kPondSize() and radius + abs(y) <= kPondSize()):
        print("error")
    else:
        t.fd(x)
        t.lt(90)
        t.fd(y)
        t.rt(90)

        t.fillcolor((random(), random(), random()))
        t.fd(radius)
        t.lt(90)
        t.down()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        t.up()
        t.rt(90)
        t.bk(radius)
        t.fillcolor("#000000")

        t.bk(x)
        t.lt(90)
        t.bk(y)
        t.rt(90)
    return 2 * pi * radius


""" Init. Conditions: Start from the center of the pond, pointing east
    Final Conditions: Back where you started, pointing east, pen up, black pen and fill
    
    Parameters: drops: Number of raindrops to draw on the pond
                radius: Set the radius of the raindrops. If it is less than or equal to 0, a random radius
                        will be chosen each time
    
    Description: draws the specified number of drops of the chosen or a random radius, each in a random color
"""
def drawNumRaindrop(drops, radius=0):
    if drops <= 0:
        return 0
    else:
        if radius <= 0:
            return drawRaindrop(randint(kMinRadius(), kMaxRadius()),
                                randint(-kPondSize() - radius, kPondSize() - radius),
                                randint(-kPondSize() - radius, kPondSize() - radius)) + drawNumRaindrop(drops - 1,
                                                                                                        radius)
        else:
            return drawRaindrop(radius,
                                randint(-kPondSize() - radius, kPondSize() - radius),
                                randint(-kPondSize() - radius, kPondSize() - radius)) + drawNumRaindrop(drops - 1,
                                                                                                        radius)
"""-----------------------------------------------------------------------------------"""

def main():
    turtleInit(0)
    pondInit()

    print("\nTotal Circumference: ", drawNumRaindrop(50))
    t.done()


main()
