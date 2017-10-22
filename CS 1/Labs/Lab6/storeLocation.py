from math import *

"""From QuickSort.py"""
"""
file: quickSort.py
version: python3
author: Arthur Nunes-Harwitt, Ivona Bezakova
purpose: Implementation of the quick-sort algorithm ( not in-place )
"""

def quickSort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition( pivot, L )
        return quickSort( less ) + same + quickSort( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e < pivot:
            less.append( e )
        elif e > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

if __name__ == "__main__":
    print( quickSort( [1, 5, 3, 4, 2, 2, 7, 5, 3, 4, 9, 0, 1, 2, 5, 4, 76, 6] ) )
"""-----------------"""


from random import *

def location(lst):
    quickSort(lst)
    median = 0
    if len(lst)%2 == 1:
        median = lst[len(lst)//2]
    else:
        median = (lst[len(lst)//2] + lst[len(lst)//2-1])/2
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
