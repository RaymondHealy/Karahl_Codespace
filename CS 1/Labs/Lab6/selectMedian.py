from random import *

def quickSelect(lst, orderFrom0):
    k = orderFrom0
    pivot = lst[len(lst)//2]
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



def main(listLength = 0):
    lst = []
    if listLength > 0:
        for i in range(listLength):
            lst += randint(0, 200)
    else:
        lst = [1, 10, 38, 214]

    print(location(lst))

main()
