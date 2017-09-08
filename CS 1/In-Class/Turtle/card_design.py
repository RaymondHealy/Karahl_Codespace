import turtle as t
""" Raymond Healy's Lab 1 Submission"""

""" Set Default State (east, up, center, speed 8) """
def initialization():
    t.speed(0)
    t.up()


"""Draw the card border from the bottom left corner, facing east"""
def draw_card_border():
    t.down()
    t.forward(170)
    t.left(90)
    t.forward(220)
    t.left(90)
    t.forward(170)
    t.left(90)
    t.forward(220)
    t.left(90)
    t.up()


"""Draw Small Club from bottom left corner of the bounding box"""
def small_club():
    t.fillcolor("Black")
    t.forward(11)
    t.down()
    t.begin_fill()
    t.forward(22)
    t.left(90)
    t.forward(22)
    t.left(90)
    t.forward(11)
    t.right(90)
    t.circle(11)
    t.right(90)
    t.circle(11)
    t.right(90)
    t.circle(11)
    t.right(90)
    t.forward(11)
    t.left(90)
    t.forward(22)
    t.left(90)
    t.end_fill()
    t.up()
    t.back(11)


"""Draw Large Club from bottom left corner of the bounding box"""
def large_club():
    t.fillcolor("Black")
    t.forward(22)
    t.down()
    t.begin_fill()
    t.forward(44)
    t.left(90)
    t.forward(44)
    t.left(90)
    t.forward(22)
    t.right(90)
    t.circle(22)
    t.right(90)
    t.circle(22)
    t.right(90)
    t.circle(22)
    t.right(90)
    t.forward(22)
    t.left(90)
    t.forward(44)
    t.left(90)
    t.end_fill()
    t.up()
    t.back(22)


"""Draw Small Diamond from bottom left corner of the bounding box"""
def small_diamond():
    t.forward(22)
    t.down()
    t.fillcolor("red")
    t.begin_fill()
    t.left(45)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(45)
    t.end_fill()
    t.up()
    t.back(22)


"""Draw Large Diamond from bottom left corner of the bounding box"""
def large_diamond():
    t.forward(44)
    t.down()
    t.fillcolor("red")
    t.begin_fill()
    t.left(45)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(45)
    t.end_fill()
    t.up()
    t.back(44)


"""Draw Number 4 from bottom left corner of the bounding box"""
def num_four():
    t.forward(22)
    t.write("4", align = "center", font = ("Arial", 15, "bold"))
    t.back(22)


"""Draw Number 2 from bottom left corner of the bounding box"""
def num_two():
    t.forward(22)
    t.write("2", align="center", font=("Arial", 15, "bold"))
    t.back(22)


"""Main Loop"""
def main():
    initialization()

    """Move to the bottom left corner of the left card"""
    t.back(190)
    t.left(90)
    t.back(110)
    t.right(90)

    """Draw the Left Card (the 4 of diamonds)"""
    draw_card_border()
    t.forward(126)
    small_diamond()
    t.back(88)
    t.left(90)
    t.forward(44)
    t.right(90)
    large_diamond()
    t.left(90)
    t.forward(88)
    t.right(90)
    t.forward(22)
    num_four()
    t.back(60)
    t.left(90)
    t.forward(44)
    t.right(90)
    small_diamond()
    t.left(90)
    t.back(176)
    t.right(90)

    """Move to the right hand card"""
    t.forward(210)

    """Draw the right hand card (the 2 of clubs)"""
    draw_card_border()
    t.forward(126)
    small_club()
    t.back(88)
    t.left(90)
    t.forward(44)
    t.right(90)
    large_club()
    t.left(90)
    t.forward(88)
    t.right(90)
    t.forward(22)
    num_two()
    t.back(60)
    t.left(90)
    t.forward(44)
    t.right(90)
    small_club()
    t.left(90)
    t.back(176)
    t.right(90)


    t.done()


main()
