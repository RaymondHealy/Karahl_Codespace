"""Raymond Healy"""

def divisible(a, b):
    if not (a > 0) and not (b > 0):
        print("Inputs must be positive integers!")
    elif a == b:
        print("Both inputs are equal")
    elif a > b:
        if a % b == 0:
            print(a, " is evenly divisible by ", b)
        else:
            print(a, " is not evenly divisible by ", b)
    else:
        if b % a == 0:
            print(b, " is evenly divisible by ", a)
        else:
            print(b, " is not evenly divisible by ", a)


def test_divisible():
    divisible(1, 2)
    divisible(2000, 150)
    divisible(20, 40)
    divisible(123123, 213123)
    divisible(7918470982137, 123412349128469128734)
    divisible(8754, 12341)


def squared(a, b):
    if a ** 2 == b:
        print(a, " squared is ", b)
    else:
        print(a, " squared is not ", b)


def test_squared():
    squared(1, 1)
    squared(2, 4)
    squared(15, 225)
    squared(1, 1)
    squared(7, 98)
    squared(12, 123123)


def main():
    test_divisible()
    test_squared()


main()
