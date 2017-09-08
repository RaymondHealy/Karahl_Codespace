import turtle as t


def zigzag(length, depth):
    depth = int(depth + .5)

    """
    Pre-Conditions: Pen down, facing to the east with respect to the final shape (first move turning 90 degrees left 
                    to north)
    Post-Conditions: Pen down, same position and orientation as initial position
    
    Arguments:  length: Leg length (in pixels) for the base fractal
                depth: How many layers to run the fractal generator for. Takes an unsigned int
                
    Description:    Draw a fractal zig-zag, 45 degrees rotated each iteration, switching colors between red and green
    """

    t.lt(90)
    if depth % 2 == 0:
        t.pencolor("#00ff00")
    else:
        t.pencolor("#ff0000")

    if depth <= 0:
        pass
    else:
        t.lt(90)
        t.fd(length / 2)
        t.rt(90)
        t.fd(length)
        zigzag(length / 2, depth - 1)
        t.bk(length)
        t.rt(90)
        t.fd(length)
        t.lt(90)
        t.bk(length)
        zigzag(length / 2, depth - 1)
        t.fd(length)
        t.lt(90)
        t.fd(length / 2)
        t.rt(90)

    if depth % 2 == 0:
        t.pencolor("#00ff00")
    else:
        t.pencolor("#ff0000")

    t.rt(90)


def main():
    """
    Pre-Conditions: Default Starting location
    Post-Conditions: Back in the same place

    Description: Makes a zig-sag style fractal with red and green coloring, leg length and depth
                 determined through user prompt
    """
    t.speed(0)
    t.right(45)
    zigzag(int(input("Leg Length: ")), int(input("Recursion Depth: ")))
    t.done()


main()
