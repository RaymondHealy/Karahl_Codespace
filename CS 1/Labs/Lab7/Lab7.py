from rit_lib import *
from quickSort import *

Box = struct_type("Box", (int , 'Capacity'), (int , 'FreeSpace'), (list, 'Items'))
Item = struct_type("Item", (str , 'Name'), (int , 'Weight'))

'''------------------------<Sort Through Lists of Structs>------------------------'''
def SortBoxes (boxLst):
    toSort = []
    for box in boxLst:
        toSort += [[box.FreeSpace, box]]
    return quickSort(toSort)

def SortItems (itemLst):
    toSort = []
    for item in itemLst:
        toSort += [[item.Weight, item]]
    return quickSort(toSort)


'''-------------------------------------------------------------------------------'''


'''-------------------------------<Read the Files>--------------------------------'''
def ReadFile (fileName):
    boxLst = []
    itemLst = []
    with open(fileName) as f:
        lines = f.readlines()
        boxes = lines[0].strip()
        lines = lines[1:]

        for element in boxes:
            boxlst += [Box(int(element), int(element), [])]

        for line in lines:
            temp = line.split()
            itemLst += [Item(temp[0], temp[1])]

    return (boxLst, itemLst)
'''-------------------------------------------------------------------------------'''

'''-----------------------------<Greedy Algorithms>-------------------------------'''
"""
    all take lists of boxes and items. Puts items into listed boxes. any 
    remaining items are left in the item list
"""
def Roomiest (itemLst, boxLst):
    remainder = []
    itemLst = SortItems(itemLst)
    for item in itemLst:
        boxLst = SortBoxes(boxLst)
        if boxLst[0].FreeSpace < item:
            remainder += [item]
        else:
            boxLst[0].Items += [item]
            boxLst[0].FreeSpace -= item.Weight
    itemLst = remainder
    return itemLst

def TightestFit (itemLst, boxLst):
    remainder = []
    itemLst = SortItems(itemLst)
    for item in itemLst:
        boxLst = SortBoxes(boxLst)
        for i in range(len(boxLst) - 1, 0, -1):
            if item.Weight <= boxLst[i].FreeSpace:
                boxLst[i].Items += [item]
                boxLst[i].FreeSpace -= item.Weight
                break
            elif i == 0:
                remainder += [item]
    itemLst = remainder

def PerBox (itemLst, boxLst):
    itemLst = SortItems(itemLst)
    boxLst = SortBoxes(boxLst)
    for box in boxLst:
        for i in range(0, len(itemLst)):
            item = itemLst[i]
            if item.Weight <= box.FreeSpace:
                itemLst = itemLst[:i] + itemLst[i + 1:]
                box.Items += [item]
                box.FreeSpace -= item.Weight

'''-------------------------------------------------------------------------------'''

def printBoxesNicely(lstBoxes, lstItems):
    if not lstItems:
        print("All Items Sorted Successfully")
    else:
        print("Unable to pack all items")

    for i in range(0, len(lstBoxes) - 1):
        box = lstBoxes[i]
        print("Box ", i + 1, ", Capacity ", box.Capacity)
        for item in box.Items:
            print("    ", item.Name, " of weight ", item.Weight)

def main():
    parsed = ReadFile(input("Enter a filename: "))
    boxLst = parsed[0]
    itemLst = parsed[1]

    print("Results from Roomiest")
    tempItems = itemLst[:]
    tempBoxes = boxLst[:]
    Roomiest(tempItems, tempBoxes)
    printBoxesNicely(tempBoxes, tempItems)
