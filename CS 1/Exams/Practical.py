import turtle as t
from random import *
from math import *
"""Raymond Healy"""
"""extra credit attempt 1: Color the fish randomly [Completed]"""
"""extra credit attempt 2: Give fish eyes [Completed]"""
"""extra credit attempt 3: Give the fish a dorsal fin [Abandoned]"""
"""extra credit attempt 4: Have the bubbles move back [Done]"""
"""extra credit attempt 5: give the fish a pectoral fin [Abandoned]"""

def init():
    t.speed(0)
    t.up()
    t.ht()

def draw_fish(r):
    t.fillcolor(random(), random(), random())
    t.rt(90)
    t.down()

    #draw the head
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    #draw the tail
    if True:
        t.rt(60)
        t.begin_fill()
        for i in range(0,3):
            t.fd(r * 1.75)
            t.rt(120)
        t.end_fill()
        t.lt(150)

    #Set fill color to black
    t.fillcolor(0, 0, 0)
    t.up()

    #Draw eye
    if True:
        t.fd(r * 1.5)
        t.lt(90)
        t.fd(r * .5)
        t.rt(90)
        t.bk(r // 5)
        t.rt(90)
        t.begin_fill()
        t.circle(r//5)
        t.end_fill()
        t.lt(90)
        t.fd(r//5)
        t.lt(90)
        t.bk(r * .5)
        t.rt(90)


def draw_bubbles(n, r):
    if n == 0:
        pass
    else:
        t.down()
        t.rt(90)
        t.circle(r)

        t.up()
        t.lt(180)
        t.fd(3*r)
        t.rt(90)
        t.bk(r)
        draw_bubbles(n - 1, r * 1.25)
        t.fd(r)
        t.lt(90)
        t.bk(3*r)
        t.rt(90)

def fish_with_bubbles(n, r):
    draw_fish(r)
    t.fd(2*r)
    t.lt(90)
    t.fd(r)
    t.rt(90)
    draw_bubbles(n, r * .25)
    t.bk(r * 2)
    t.lt(90)
    t.bk(r)
    t.rt(90)

def fish_tank(num_fishes):
    for i in range(0, num_fishes):
        x = randint(0, 600)
        y = randint(0, 600)
        t.fd(x - 300)
        t.lt(90)
        t.fd(y - 300)
        t.rt(90)
        fish_with_bubbles(randint(2, 5), randint(10, 50))
        t.lt(90)
        t.bk(y - 300)
        t.rt(90)
        t.bk(x - 300)

def main():
    init()
    fish_tank(5)
    t.done()

main()