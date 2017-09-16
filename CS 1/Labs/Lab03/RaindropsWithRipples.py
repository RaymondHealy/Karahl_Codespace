import turtle as t
from random import *
from math import *

"""------------------------------------<Constants>------------------------------------"""
"""Defines the absolute value of the max and min of the pond bounding box"""
def kPondSize():
    return 250

"""Defines the minimum random radius of the raindrops"""
def kMinRadius():
    return 1

"""Defines the maximum random radius of the raindrops"""
def kMaxRadius():
    return 15

"""Defines the number of ripples"""
def kNumRipples():
    return 5

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

"""----------------------------<Raindrop Ripple Functions>----------------------------"""
""" Init. Conditions: Start from the center of the pond. pointing East
    Final Conditions: Back where you started, same orientation, pen up, black fill and pen colors

    Parameters: radius: Radius of the circle to be drawn
                x: x displacement from the origin in pixels
                y: y displacement from the origin in pixels
                
    Returns: The Radius of the raindrop and its ripples

    Description: Draws a rain drop of the specified radius at displacement (X,Y) from the origin with a random color
"""
def drawRaindropWithRipples(radius, x, y, numRipples=kNumRipples()):
    """If the ripples would go out of bounds, then re-roll"""
    if not (radius * (numRipples + 1) + abs(x) <= kPondSize() and radius * (numRipples + 1) + abs(y) <= kPondSize()):
        """Reroll the raindrop"""
        return drawRaindropWithRipples(randint(kMinRadius(), kMaxRadius()), randint(-kPondSize(), kPondSize()),
                                       randint(-kPondSize(), kPondSize()), numRipples)
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

        return 2 * pi * radius + drawRipple(numRipples, radius, 2*radius) + goHome(x, y)

""" Init. Conditions: Start from the center of the pond, pointing east
    Final Conditions: Back where you started, pointing east, pen up, black pen and fill

    Parameters: drops: Number of raindrops to draw on the pond
                radius: Set the radius of the raindrops. If it is less than or equal to 0, a random radius
                        will be chosen each time
                        
    Returns: The sum of the circumferences of the raindrops and their ripples

    Description: draws the specified number of drops of the chosen or a random radius, each in a random color
                 Non-Tail Recursion
"""
def drawNumRaindrop(drops, radius=0):
    if drops <= 0:
        return 0
    else:
        if radius <= 0:
            return drawRaindropWithRipples(randint(kMinRadius(), kMaxRadius()),
                                           randint(-kPondSize() - radius, kPondSize() - radius),
                                           randint(-kPondSize() - radius, kPondSize() - radius)) + drawNumRaindrop(
                drops - 1,
                radius)
        else:
            return drawRaindropWithRipples(radius,
                                           randint(-kPondSize() - radius, kPondSize() - radius),
                                           randint(-kPondSize() - radius, kPondSize() - radius)) + drawNumRaindrop(
                drops - 1,
                radius)

""" Init. Conditions: Start in the center of the raindrop, facing east, pen up
    Final Conditions: Center of the raindrop, facing east, pen up, ripples drawn
    
    Parameters: ripplesLeft: Number of Recursive Layers Left
                baseRadius: Base Radius of the raindrop
                radius: Radius of the circle to be drawn
                sum: The accumulator, allows tail recursion
                
    Returns: sum of the circumferences of the ripples
    
    Description: Draws the ripples for the raindrop with tail recursion
"""
def drawRipple(ripplesLeft, baseRadius, radius, accumulator = 0):
    if ripplesLeft <= 0:
        return accumulator
    else:
        t.fd(radius)
        t.lt(90)
        t.down()
        t.circle(radius)
        t.up()
        t.rt(90)
        t.bk(radius)
        return drawRipple(ripplesLeft-1, baseRadius, radius+baseRadius,  float(accumulator) + 2*pi*radius)

""" Init. Conditions: Center of raindrop, after the ripples have been drawn pen up
    Final Conditions: Origin (center of the pond/initial position), facing east (right) pen up
    
    Parameters: x: The x coordinate of the raindrop's center
                y: The y coordinate of the raindrop's center
                
    Returns: 0, inserts right into the return statement of drawNumRaindrop, allows combination of the 
    
    Description: Returns the turtle cursor home after drawing the ripples, allows it to happen alongside the summation
"""
def goHome (x, y):
    t.up()
    t.bk(x)
    t.lt(90)
    t.bk(y)
    t.rt(90)
    t.fillcolor("#000000")

    return 0

"""-----------------------------------------------------------------------------------"""

""" Init. Conditions: Default state
    Final Conditions: Painting done, back at origin
    
    Parameters: None
    
    Returns: None (prints the total circumference of all ripples and drops to the console)
    
    Description: Draw a box for the pond, prompt the user for a number of drops, draw those drops and their ripples, 
                 and print the sum of their circumferences to the console.
"""
def main():
    turtleInit()
    pondInit()

    numDrops = int(input("Number of drops, 1-100 inclusive: "))
    if 100 >= numDrops >= 1:
        print("The Total Circumference of all ripples is ",drawNumRaindrop(numDrops), " units.\nClose the window to quit.")
    else:
        print("Invalid, enter a number between 1 and 100")
        main()  # Try again for a valid answer

    t.done()


main()
