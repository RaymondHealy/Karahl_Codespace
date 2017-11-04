from linked_code import *

"""Raymond Healy"""

"""
The process of finding the minimum value in linked list <<lnk>>
Do not call directly. <<minVal>> is the minimum value so far.
Non-Destructive
"""


def find_min_value_recursive(lnk, minVal):
    if lnk == None:
        return minVal
    else:
        if lnk.value < minVal:
            minVal = lnk.value
        return find_min_value_recursive(lnk.rest, minVal)


"""
The function to start the process of finding the minimum
value of linked list <<lnk>>. If given a <<None>>, it 
will return <<None>>. Otherwise, it returns the minimum 
value. 
Non-Destructive
"""


def find_min_value(lnk):
    if not lnk:
        return None
    else:
        return find_min_value_recursive(lnk.rest, lnk.value)


"""
Returns a sorted linked list of << linked_code.py >>
<< Nodes >> from unsorted linked list << lnk >>
Non-Destructive
"""


def link_sort(lnk):
    sortedLnk = None
    nextVal = find_min_value(lnk)

    while nextVal != None:  # While the minimum remaining value isn't a << None >>
        sortedLnk = cat(sortedLnk, Node(nextVal, None))  # add the next value to the list
        lnk = remove(nextVal, lnk)  # Remove the value just added to the sorted list
        nextVal = find_min_value(lnk)  # Get the next value to add

    return sortedLnk


"""

"""


def pretty_print(lnk):
    if lnk == None:
        print("None")
        return None

    print("[", end='')
    nextVal = lnk.value

    while lnk != None:
        print(nextVal, end='')

        lnk = lnk.rest
        if lnk != None:
            print(', ', end='')
            nextVal = lnk.value
    print(']')
    return None
