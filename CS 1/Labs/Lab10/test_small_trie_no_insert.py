"""
File: test_small_trie_no_insert.py
description: Program to test Trie tree functionality.

Author:  CS @ RIT
"""

from trie import *


def test():
    """
    test functions on a small trie not using insert function
    """
    print("test small trie no insert")

    X1 = "001010"
    X2 = "000111"
    X3 = "111000"
    X4 = "010000"
    X5 = "110001"

    # build the trie manually
    t1 = Trie(None, X1, None)
    t2 = Trie(None, X2, None)
    t3 = Trie(None, X3, None)
    t4 = Trie(None, X4, None)
    t5 = Trie(None, X5, None)
    t21 = Trie(t2, "", t1)
    t214 = Trie(t21, "", t4)
    t53 = Trie(t5, "", t3)
    t53a = Trie(None, "", t53)
    trie = Trie(t214, "", t53a)


    print("test trie_to_list()")
    print([X2, X1, X4, X5, X3] == trie_to_list(trie))
    print([X2, X1, X4] == trie_to_list(trie.left))
    print([X5, X3] == trie_to_list(trie.right))

    print("test smallest()")
    print(X2 == smallest(trie))
    print(X5 == smallest(trie.right))

    print("test largest()")
    print(X3 == largest(trie))
    print(X4 == largest(trie.left))

    print("test search()")
    print(X1 == search(trie, X1))
    print(X3 == search(trie, "111011"))
    print(X5 == search(trie, "101111"))
    print(X4 == search(trie, "011111"))

    print("test height()")
    print(0 == height(None))
    print(0 == height(Trie(None, X1, None)))
    print(3 == height(trie))

    print("test size()")
    print(0 == size(None))
    print(1 == size(Trie(None, X1, None)))
    print(5 == size(trie))


# run the test
test()