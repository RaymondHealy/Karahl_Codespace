#         Raymond Healy
import turtle as t


# ------------------------------------------------------------------------------------------------------------------------------------------
def init(spd=10):
    t.speed(spd)
    t.up()


# ------------------------------------------------------------------------------------------------------------------------------------------
def regularPolygon(numSides, sideLength):
    t.down()
    numSides = int(numSides + .5)
    if numSides >= 3:
        counter = 1
        angleMeasure = (numSides - 2) * 180 / numSides - 180
        while counter <= numSides:
            t.forward(sideLength)
            t.left(angleMeasure)
            counter = counter + 1
    else:
        print("ERROR, Too Few Sides, At least 3 needed")
    t.up()


# ------------------------------------------------------------------------------------------------------------------------------------------
def regularPolygonCentered(numSides, sideLength):
    t.down()
    numSides = int(numSides + .5)
    if numSides >= 3:
        counter = 1
        angleMeasure = (numSides - 2) * 180 / numSides - 180
        t.forward(int(sideLength / 2))
        t.left(angleMeasure)
        while counter < numSides:
            t.forward(sideLength)
            t.left(angleMeasure)
            counter = counter + 1
        if sideLength / 2 == int(sideLength / 2):
            t.forward(int(sideLength / 2))
        else:
            t.forward(int(sideLength / 2) + 1)
    else:
        print("ERROR, Too Few Sides, At least 3 needed")

# ------------------------------------------------------------------------------------------------------------------------------------------


def main():
    sideLength = 150
    init(8)

    t.begin_fill()
    regularPolygonCentered(3, sideLength)
    t.end_fill()
    t.done()


# ------------------------------------------------------------------------------------------------------------------------------------------
main()
