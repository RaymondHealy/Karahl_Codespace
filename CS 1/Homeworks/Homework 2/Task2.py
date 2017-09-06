"""Raymond Healy"""

def squared(a, b):
    if a**2 == b:
        print(a," squared is ",b)
    else:
        print(a, " squared is not ", b)

def squared_test():
    squared(1,1)
    squared(2,4)
    squared(15,225)
    squared(1,1)
    squared(7,98)
    squared(12,123123)

squared_test()