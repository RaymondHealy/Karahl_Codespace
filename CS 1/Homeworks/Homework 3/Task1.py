"""Raymond Healy"""

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


def main ():
    sumSquaresTest()

main()