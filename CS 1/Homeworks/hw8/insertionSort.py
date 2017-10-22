"""
Sorts the given list from least to greatest
"""
def InsertionSort (lst):
    lstCpy = lst[:]

    for i in range(0, len(lstCpy) - 1): # for all values i which are valid indexes in lstCpy
        Insert(lstCpy, i) # Move the item at index i to its
                       #  proper index less than i

    return lstCpy

def Swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp

def Insert(lst, mark):
    index = mark #start sorting at the mark
    while index >= 0 and lst[index] > lst[index + 1]:   # While before the end of the list, and the current focus isn't
                                                        #  far enough along
        Swap(lst, index, index+1)   # Swap the focus object and the next object in sequence to
                                    #  put them in increasing order
        index -= 1  # Shift the focus back 1 to compare the newly swapped
                    # entry with the previous portion of the list
