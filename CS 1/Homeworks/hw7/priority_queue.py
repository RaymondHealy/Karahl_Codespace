from random import *
"""Raymond Healy"""

"""
1.2.1
    * you must find where you want to insert, and insert the new data surrounded by the old into the 
      slice containing the 2 border values or swap up/down the chain, storing overridden data as you
      go along 

    * removing from the end of the list is easier, because you need only shrink the size by the number
      removed, and not shift the entire list down

1.4
    1. O(1)
    2. O(Log(N))
    3. O(N)
    4. O(1)
    5. Better, the search especially is better because it is ordered (needs to be for binary)
"""

def enqueue(lst, item):
    """default the position to 0. if it is not empty, use binary search to find the correct position"""
    position = positionSearch(lst, item, 0, len(lst) - 1)

    lst += [item]
    if not len(lst) == position:
        for i in range(len(lst) - 1, position, -1):
            swap(lst, i, i-1)

def positionSearch (lst, target, start, end):
    if not lst: #if the list is empty, tell it to write to slot 0
        return 0
    elif target > lst[0]: #check if the target has the lowest priority
        return 0
    elif target < lst[len(lst) - 1]:
        return len(lst)
    else:
        if start - end == 1: #if narrowed down to 1 option
            return start
        elif start > end:
            return None

        midIndex = (start + end) // 2
        midVal = lst[midIndex]
        if target == midVal:
            return midIndex
        elif target > midVal:
            return positionSearch(lst, target, start, midIndex - 1)
        else:
            return positionSearch(lst, target, midIndex + 1, end)

def swap (lst, i, j):
    temp = lst[j]
    lst [j] = lst[i]
    lst[i] = temp

def dequeue(lst):
    if len(lst) > 0:
        return lst.pop(-1)
    else:
        return None

def randTest( numEntries, list):
    for i in range(numEntries):
        enqueue(list, randint(0, 100))

    print("Queue is: ", list)
    print("Highest priority item is", dequeue(list))
    print("Next highest priority task is", dequeue(list))

def main():
    pQueue = []
    randTest(20, pQueue)
    pQueue = []
    randTest(0, pQueue)
    randTest(20, pQueue)
    pQueue = []
    randTest(1, pQueue)

main()