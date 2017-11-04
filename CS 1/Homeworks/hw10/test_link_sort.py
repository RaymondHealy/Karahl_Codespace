from link_sort import *

"""
Takes a text file with one integer per line and turns it to a linked
list
"""


def read_file(filename):
    lnk = None

    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            value = int(line.strip())
            lnk = cat(lnk, Node(value, None))
            0
        f.close()

    return lnk


def main():
    filename = input('Filename to sort from: ').strip()
    while filename != '':
        unsortedLnk = read_file(filename)
        print(unsortedLnk)
        sortedLnk = link_sort(unsortedLnk)
        print(sortedLnk)

        pretty_print(unsortedLnk)
        pretty_print(sortedLnk)

        filename = input('Filename to sort from: ').strip()


main()
