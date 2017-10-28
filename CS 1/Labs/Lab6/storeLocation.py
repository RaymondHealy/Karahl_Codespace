from quickSort import *
from time import *


def location(lst):
    quickSort(lst)
    median = 0
    if len(lst) % 2 == 1:
        median = lst[len(lst) // 2]
    else:
        median = (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    return median


def parseTxtList(filename):
    distances = []

    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            distances += [float(line.split()[1])]
    return distances


def main(timesToRun = 20):
    lst = parseTxtList('TestList.txt')
    start = time()
    loc = location(lst)
    end = time()

    total = 0
    for item in lst:
        total += abs(loc - item)
    avgDist = total / len(lst)

    print("Optimum Location        : ", loc)
    print("Average Distance to Loc : ", avgDist, "\n")

    total = 0
    for i in range(timesToRun):
        total += end - start
        print("Time to Find            : ", end - start, " seconds")
        start = time()
        location(lst)
        end = time()
    print("\nAverage Time            : ", total / timesToRun, " seconds")




main()
