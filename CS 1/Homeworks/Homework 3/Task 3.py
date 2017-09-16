"""Raymond Healy"""

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: n: number of stairs to climb

    Returns: number of possible ways to climb "n" stairs

    Description: returns the number of possible ways to climb "n" stairs, determined through non-tail-recursion
"""
def stairClimb (n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return stairClimb(n-1)+stairClimb(n-2)+stairClimb(n-3)

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: n: number of stairs to climb
                acc: running total of the possible ways to climb

    Returns: number of possible ways to climb "n" stairs

    Description: returns the number of possible ways to climb "n" stairs, determined through tail-recursion
"""
def stairClimbAcc(n, a = 1, b = 2, c = 4):
    if n <= 0:
        return 0
    elif n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c
    else:
        return stairClimbAcc(n-1, b, c, a + b + c)

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: n: number of stairs to climb

    Returns: number of possible ways to climb "n" stairs

    Description: calls "stairClimbAcc()" with the specified n and the default values for a, b, and c
"""
def stairClimbTR(n):
    return stairClimbAcc(n)

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: NA

    Returns: NA (prints to command Prompt)

    Description: runs both stair climb algorithms for n=0 through n=6
"""
def stairClimbTest():
    print("Results of the sum of squares test")
    print("n == 0: ", stairClimb(0), "  ,  ", stairClimbTR(0))
    print("n == 1: ", stairClimb(1), "  ,  ", stairClimbTR(1))
    print("n == 2: ", stairClimb(2), "  ,  ", stairClimbTR(2))
    print("n == 3: ", stairClimb(3), "  ,  ", stairClimbTR(3))
    print("n == 4: ", stairClimb(4), "  ,  ", stairClimbTR(4))
    print("n == 5: ", stairClimb(5), "  ,  ", stairClimbTR(5))
    print("n == 6: ", stairClimb(6), "  ,  ", stairClimbTR(6))

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: n: How many squares to add together

    Returns: the sum of the first "n" perfect squares

    Description: Non-tail recursive summation of the first "n" perfect squares
"""
def sumSquares(n):
    n = abs(int(n+.5))
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n ** 2 + sumSquares(n - 1)

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: n: How many squares to add together
                acc: the running total

    Returns: the sum of the first "n" perfect squares

    Description: Tail recursive summation of the first "n" perfect squares
"""
def sumSquaresAccum(n, acc = 0):
    if n <= 0:
        return 0
    elif n == 1:
        return acc + 1
    else:
        return sumSquaresAccum(n-1, acc + n**2)

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: n: How many squares to add together

    Returns: the sum of the first "n" perfect squares

    Description: Calls "sumSquaresAccum()" with an initial "acc" of 0, passing "n" directly through
"""
def sumSquaresTR(n):
    return sumSquaresAccum(n)

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: NA

    Returns: NA (prints to command prompt)

    Description: Prints the results of the sum of squares functions for n=0 through n=6
"""
def sumSquaresTest():
    print("Results of the sum of squares test")
    print("n == 0: ", sumSquares(0), "  ,  ", sumSquaresTR(0))
    print("n == 1: ", sumSquares(1), "  ,  ", sumSquaresTR(1))
    print("n == 2: ", sumSquares(2), "  ,  ", sumSquaresTR(2))
    print("n == 3: ", sumSquares(3), "  ,  ", sumSquaresTR(3))
    print("n == 4: ", sumSquares(4), "  ,  ", sumSquaresTR(4))
    print("n == 5: ", sumSquares(5), "  ,  ", sumSquaresTR(5))
    print("n == 6: ", sumSquares(6), "  ,  ", sumSquaresTR(6))

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: NA

    Returns: NA

    Description: runs "stairClimbTest()" and "sumSquaresTest()"
"""
def main ():
    stairClimbTest()
    print("\n\n")
    sumSquaresTest()

main()