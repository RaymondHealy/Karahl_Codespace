import turtle as t

def drawTree (segments, length):
    segments = int(segments + .5)

    if segments <= 0:
        pass
    elif segments == 1:
        t.down()
        t.forward(length)
        t.back(length)
    else:
        t.down()
        t.forward(length)
        t.left(45)
        drawTree(segments - 1, length / 1.5)
        t.right(90)
        drawTree(segments - 1, length / 1.5)
        t.left(45)
        t.back(length)
    t.up

def main():
    segments = int(input("How Many Segments:"))
    length = int(input("Segment Length:"))
    t.speed(0)
    loop = 1
    t.tracer(0,0)
    while loop<=4:
        t.left(90)
        drawTree(segments, length)
        loop = loop+1
    t.update()
    t.done()

main()