"""Raymond Healy"""

import random as r
import time as t

from insertionSort import *
from quickSort import *
from mergeSort import *



def GenerateRandomList(size, minimum, maximum):
    toReturn = []
    for i in range(0, size-1):
        toReturn += [r.randint(minimum, maximum)]
    return toReturn

def test_insertion_sort():
    unsortedList = GenerateRandomList(10, 0, 30)
    sortedList =  InsertionSort(unsortedList)
    if max(sortedList) == sortedList[-1]:
        print("InsertionSort was Correct")
    else:
        print("InsertionSort was Incorrect")

def test_quick_sort():
    unsortedList = GenerateRandomList(10, 0, 30)
    sortedList =  quickSort(unsortedList)
    if max(sortedList) == sortedList[-1]:
        print("quickSort was Correct")
    else:
        print("quickSort was Incorrect")

def test_merge_sort():
    unsortedList = GenerateRandomList(10, 0, 30)
    sortedList =  mergeSort(unsortedList)
    if max(sortedList) == sortedList[-1]:
        print("mergeSort was Correct")
    else:
        print("mergeSort was Incorrect")

def main():
    quickSortMaxedOut = False
    mergeSortMaxedOut = False
    insertionSortMaxedOut = False

    listSize = int(input("Initial List Size: "))
    minValue = int(input("Min Item Size    : "))
    maxValue = int(input("Max Item Size    : "))
    while not quickSortMaxedOut or not mergeSortMaxedOut or not insertionSortMaxedOut:
        unsortedList = GenerateRandomList(listSize, minValue, maxValue)

        print("\n============================================================")
        print("List Size: ", listSize)
        print("------------------------------")
        if not insertionSortMaxedOut:
            start = t.time()
            InsertionSort(unsortedList)
            end = t.time()
            print("Insertion Sort Time: ", end - start)
            insertionSortMaxedOut = end - start >= 1
        if not quickSortMaxedOut:
            start = t.time()
            quickSort(unsortedList)
            end = t.time()
            print("Quick Sort Time    : ", end - start)
            quickSortMaxedOut = end - start >= 1
        if not mergeSortMaxedOut:
            start = t.time()
            mergeSort(unsortedList)
            end = t.time()
            print("Merge Sort Time    : ", end - start)
            mergeSortMaxedOut = end - start >= 1

        print("============================================================")
        listSize = listSize * 10


main()