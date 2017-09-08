import turtle as t


def zigzag(length, depth):
    """
    Pre-Conditions: Default Starting location
    Post-Conditions: Back in the same place

    Description:    Makes a zig-sag style fractal with red and green coloring, leg length and depth
                    determined through user prompt
    """
    depth = int(depth + .5)
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


def main():
    """
    Pre-Conditions: Default Starting location
    Post-Conditions: Back in the same place

    Description: Makes a zig-sag style fractal, leg length and depth determined through user prompt
    """

    t.speed(0)
    zigzag(int(input("Leg Length: ")), int(input("Recursion Depth: ")))
    t.done()


main()
