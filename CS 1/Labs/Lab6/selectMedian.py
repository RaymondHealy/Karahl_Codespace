from time import *
from random import *

def quickSelect(lst, orderFrom0):
    k = orderFrom0
    pivot = lst[randint(0, len(lst) - 1)]
    smallerList = []
    largerList = []
    count = 0
    
    for element in lst:
        if element == pivot:
            count += 1
        elif element > pivot:
            largerList += [element]
        else:
            smallerList += [element]
            
    m = len(smallerList)

    if k >= m and k < m + count:
        return pivot
    elif m > k:
        return quickSelect(smallerList, k)
    else:
        return quickSelect(largerList, k - m - count)

def location(lst):
    median = 0
    if len(lst)%2 == 1:
        median = quickSelect(lst, len(lst)//2)
    else:
        median = (quickSelect(lst, len(lst)//2) + quickSelect(lst, len(lst)//2-1))/2
    return median

def parseTxtList (filename):
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
