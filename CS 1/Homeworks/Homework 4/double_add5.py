from random import *


def print_sequence_rec(start, count):
    count = abs(int(count + .5))
    if count <= 0:
        print(start)
    else:
        print(start)
        print_sequence_rec(start * 2 + 5, count - 1)


def print_sequence_itr(start, count):
    count = abs(int(count + .5))

    i = 0
    val = start
    while i <= count:
        print(val)
        val = val * 2 + 5
        i += 1


def find_start_forward(goal, count):
    count = abs(int(count + .5))

    startValue = 0
    gotIt = False;
    while not gotIt:
        i = 1
        value = startValue
        while value < goal and i <= count and not gotIt:
            value = value * 2 + 5
            if value >= goal:
                gotIt = True
                break
            i += 1

        if gotIt:
            break
        else:
            startValue += 1
    return startValue


def find_back_limit_rec(nbr, count):
    if count <= 0:
        if int(nbr) == nbr:
            return int(nbr)
        else:
            return int(nbr) + 1
    else:
        return find_back_limit_rec((nbr - 5) / 2, count - 1)


def find_back_limit_iter(nbr, count):
    i = 0
    nbr = nbr
    while i < count:
        nbr = (nbr - 5) / 2
        i += 1

    if not int(nbr) == nbr:
        nbr = int(nbr) + 1
    return int(nbr)


def test(minNum=1, maxNum=100, minCnt=1, maxCnt=5, numCycles=5):
    i = 1
    while i <= numCycles:
        num = randint(minNum, maxNum)
        count = randint(minCnt, maxCnt)
        print("\n\n\n--------------------------Test Number ", i, " Of ", numCycles, "-------------------------")
        print("Base Number = ", num)
        print("Number Of Cycles = ", count)
        print("--Find Sequence Recursively---")
        print_sequence_rec(num, count)
        print("\n---Find Sequence Iteratively---")
        print_sequence_itr(num, count)
        print("\n---Fruitful Functions---")
        print("minimum starting value to reach ", num, " in ", count, " steps:\n",
              "          ", find_start_forward(num, count))
        foo = find_back_limit_rec(num, count)
        bar = find_back_limit_iter(num, count)
        print("Minimum starting value that gets you to ", num, " in ", count, " steps:\n",
              "          Recursive: ", foo, '\n',
              "          Iterative: ", bar)
        if foo == bar:
            print("          ---------They Match---------")
        else:
            print("          ------They Don't Match------")

        i += 1
        print("---------------------------------------------------------------------")


test()
