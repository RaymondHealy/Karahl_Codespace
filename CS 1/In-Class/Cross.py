import turtle as t

def initialize(speed = 0):
    t.speed(speed)

def drawCross(length, depth):
    length = int(length + .5)
    depth = int(depth + .5)
    t.down()

    if depth <= 0:
        pass
    else:
        t.fd(length * 4 / 5)
        t.lt(90)
        t.fd(length/4)
        drawCross(length/2, depth-1)
        t.bk(length/2)
        t.lt(180)
        drawCross(length/2, depth-1)
        t.bk(length/4)
        t.left(90)
        t.fd(length/5)
        drawCross(length/2, depth-1)
        t.bk(length)

def main():
    initialize(0)
    t.fd(50)
    drawCross(100, 5)
    t.bk(50)
    t.done()

main()