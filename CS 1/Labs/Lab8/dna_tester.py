"""
Program to test DNA linked Node functionality.

Author:  CS @ RIT
File: dna_tester.py
"""

import dna
import linked_code  # in case student's dna module didn't import


def test1():
    """
    Tests function to convert a string
    into a DNA linked Node structure.
    :return: None
    """
    print("Test1: testing convert_to_nodes")

    dna_seq1 = dna.convert_to_nodes("")
    print(dna_seq1 == None, end=" ")

    dna_seq2 = dna.convert_to_nodes("A")
    print(dna_seq2.value == "A" and dna_seq2.rest == None, end=" ")

    dna_seq3 = dna.convert_to_nodes("GTC")
    print(dna_seq3.value == 'G' and dna_seq3.rest.value == 'T'
          and dna_seq3.rest.rest.value == 'C' and
          dna_seq3.rest.rest.rest == None)


def test2():
    """
    Tests function to convert a DNA linked Node
    structure into a string.
    :return:
    """

    print("Test2: testing convert_to_string")

    dna_str1 = dna.convert_to_string(None)
    print(dna_str1 == "", end=" ")

    dna_seq = None
    dna_seq = linked_code.insertAt(0, "C", dna_seq)
    dna_str2 = dna.convert_to_string(dna_seq)
    print(dna_str2 == "C", end=" ")

    dna_seq = None
    dna_seq = linked_code.insertAt(0, 'T', dna_seq)
    dna_seq = linked_code.insertAt(1, 'A', dna_seq)
    dna_seq = linked_code.insertAt(2, 'G', dna_seq)
    dna_str3 = dna.convert_to_string(dna_seq)
    print(dna_str3 == "TAG")


def test3():
    """
    Tests is_match function.
    :return: None
    """

    print("Test3: testing is_match")

    dna_seq1 = None
    dna_seq2 = None

    print(dna.is_match(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq2 = linked_code.insertAt(0, "A", dna_seq2)
    print(dna.is_match(dna_seq1, dna_seq2) == False, end=" ")
    print(dna.is_match(dna_seq2, dna_seq1) == False, end=" ")

    dna_seq1 = linked_code.insertAt(0, "A", dna_seq1)
    print(dna.is_match(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = linked_code.insertAt(1, "T", dna_seq1)
    dna_seq1 = linked_code.insertAt(2, "G", dna_seq1)
    dna_seq1 = linked_code.insertAt(3, "C", dna_seq1)
    dna_seq2 = linked_code.insertAt(1, "T", dna_seq2)
    dna_seq2 = linked_code.insertAt(2, "G", dna_seq2)
    print(dna.is_match(dna_seq1, dna_seq2) == False, end=" ")
    dna_seq2 = linked_code.insertAt(3, "C", dna_seq2)
    print(dna.is_match(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = linked_code.insertAt(2, "A", dna_seq1)
    dna_seq2 = linked_code.insertAt(2, "G", dna_seq2)
    print(dna.is_match(dna_seq1, dna_seq2) == False)


def test4():
    """
    Tests is_pairing function.
    :return: None
    """

    print("Test4: testing is_pairing")

    dna_seq1 = None
    dna_seq2 = None

    print(dna.is_pairing(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq2 = linked_code.insertAt(0, "A", dna_seq2)
    print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")
    print(dna.is_pairing(dna_seq2, dna_seq1) == False, end=" ")

    dna_seq1 = linked_code.insertAt(0, "T", dna_seq1)
    print(dna.is_pairing(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = linked_code.insertAt(1, "T", dna_seq1)
    dna_seq1 = linked_code.insertAt(2, "G", dna_seq1)
    dna_seq1 = linked_code.insertAt(3, "C", dna_seq1)
    dna_seq2 = linked_code.insertAt(1, "A", dna_seq2)
    dna_seq2 = linked_code.insertAt(2, "C", dna_seq2)
    print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")
    dna_seq2 = linked_code.insertAt(3, "G", dna_seq2)
    print(dna.is_pairing(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = linked_code.insertAt(2, "A", dna_seq1)
    dna_seq2 = linked_code.insertAt(2, "A", dna_seq2)
    print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")

    test_str1 = "AATTTGC"
    test_str2 = "GCGCTGC"

    for idx in range(len(test_str1)):
        dna_seq1 = linked_code.removeAt(2, dna_seq1)
        dna_seq2 = linked_code.removeAt(2, dna_seq2)
        dna_seq1 = linked_code.insertAt(2, test_str1[idx], dna_seq1)
        dna_seq2 = linked_code.insertAt(2, test_str2[idx], dna_seq2)
        print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")

    print()


def test5():
    """
    Tests is_palindrome function.
    :return: None
    """

    print("Test5: testing is_palindrome")

    dna_seq = None
    print(dna.is_palindrome(dna_seq) == True, end=" ")

    dna_seq = linked_code.insertAt(0, "A", dna_seq)
    print(dna.is_palindrome(dna_seq) == True, end=" ")

    dna_seq = linked_code.insertAt(0, "T", dna_seq)
    print(dna.is_palindrome(dna_seq) == False, end=" ")

    dna_seq = linked_code.removeAt(0, dna_seq)
    dna_seq = linked_code.insertAt(0, "A", dna_seq)
    print(dna.is_palindrome(dna_seq) == True, end=" ")

    dna_seq = linked_code.insertAt(1, "G", dna_seq)
    print(dna.is_palindrome(dna_seq) == True, end=" ")

    dna_seq = linked_code.insertAt(2, "T", dna_seq)
    print(dna.is_palindrome(dna_seq) == False)


def test6():
    """
    Tests substitution function.
    :return: None
    """

    print("Test6: testing substitution")

    dna_seq = None
    try:
        dna_seq = dna.substitution(dna_seq, 0, "A")
        print("False", end=" ")  # failed to catch exception
    except:
        print("True", end=" ")

    dna_seq = linked_code.insertAt(0, "A", dna_seq)
    dna_seq2 = dna.substitution(dna_seq, 0, "T")
    print(dna_seq2.value == "T", end=" ")

    dna_seq = linked_code.insertAt(1, "T", dna_seq)
    dna_seq2 = dna.substitution(dna_seq, 1, "G")
    print(dna_seq2.value == "A" and dna_seq2.rest.value == "G", end=" ")

    dna_seq = linked_code.insertAt(2, "G", dna_seq)
    dna_seq = linked_code.insertAt(3, "C", dna_seq)
    try:
        dna_seq2 = dna.substitution(dna_seq, 4, "A")
        print("False", end=" ")  # failed to catch exception
    except:
        print("True", end=" ")
    dna_seq2 = dna.substitution(dna_seq, 2, "A")
    print(dna_seq2.value == "A" and dna_seq2.rest.value == "T" \
          and dna_seq2.rest.rest.value == "A")


def test7():
    """
    Tests insertion function.
    :return: None
    """

    print("Test7: testing insertion")

    dna_seq1 = None
    dna_seq2 = None
    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3 == None, end=" ")

    try:
        dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
        print("False", end=" ")  # failed to catch exception
    except:
        print("True", end=" ")

    dna_seq1 = linked_code.insertAt(0, "A", dna_seq1)
    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3.value == "A" \
          and linked_code.lengthRec(dna_seq3) == 1, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
    print(dna_seq3.value == "A" \
          and linked_code.lengthRec(dna_seq3) == 1, end=" ")

    dna_seq2 = linked_code.insertAt(0, "C", dna_seq2)
    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3.value == "C" and dna_seq3.rest.value == "A" \
          and linked_code.lengthRec(dna_seq3) == 2, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
    print(dna_seq3.value == "A" and dna_seq3.rest.value == "C" \
          and linked_code.lengthRec(dna_seq3) == 2, end=" ")

    dna_seq1 = linked_code.insertAt(0, "T", dna_seq1)  # now TA
    dna_seq2 = linked_code.insertAt(0, "G", dna_seq2)  # now GC

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3.value == "G" and dna_seq3.rest.value == "C" \
          and dna_seq3.rest.rest.value == "T" \
          and dna_seq3.rest.rest.rest.value == "A"
          and linked_code.lengthRec(dna_seq3) == 4, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
    print(dna_seq3.value == "T" and dna_seq3.rest.value == "G" \
          and dna_seq3.rest.rest.value == "C" \
          and dna_seq3.rest.rest.rest.value == "A"
          and linked_code.lengthRec(dna_seq3) == 4, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 2)
    print(dna_seq3.value == "T" and dna_seq3.rest.value == "A" \
          and dna_seq3.rest.rest.value == "G" \
          and dna_seq3.rest.rest.rest.value == "C"
          and linked_code.lengthRec(dna_seq3) == 4)


def test8():
    """
    Tests deletion function.
    :return: None
    """

    print("Test8: testing deletion")

    dna_seq1 = None
    dna_seq2 = dna.deletion(dna_seq1, 0, 0)
    print(dna_seq2 == None, end=" ")

    try:
        dna_seq2 = dna.deletion(dna_seq1, 0, 1)
        print("False", end=" ")  # failed to catch exception
    except:
        print("True", end=" ")

    dna_seq1 = linked_code.insertAt(0, "A", dna_seq1)
    dna_seq2 = dna.deletion(dna_seq1, 2, 0)
    print(dna_seq2.value == "A" and \
          linked_code.lengthRec(dna_seq2) == 1, end=" ")

    dna_seq2 = dna.deletion(dna_seq1, 0, 1)
    print(dna_seq2 == None, end=" ")

    dna_seq1 = linked_code.insertAt(1, "T", dna_seq1)
    dna_seq1 = linked_code.insertAt(2, "G", dna_seq1)
    dna_seq1 = linked_code.insertAt(3, "C", dna_seq1)
    dna_seq2 = dna.deletion(dna_seq1, 0, 1)
    print(dna_seq2.value == "T" and \
          linked_code.lengthRec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 1, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "G" and \
          linked_code.lengthRec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 2, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 3, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "G" and \
          linked_code.lengthRec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 0, 2)
    print(dna_seq2.value == "G" and \
          dna_seq2.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 2, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 1, 2)
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 2, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 2, 2)
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          linked_code.lengthRec(dna_seq2) == 2, end=" ")

    try:
        dna_seq2 = dna.deletion(dna_seq1, 3, 2)
        print("False", end=" ")  # failed to catch exception
    except:
        print("True", end=" ")

    dna_seq2 = dna.deletion(dna_seq1, 0, 3)
    print(dna_seq2.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 1, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 1, 3)
    print(dna_seq2.value == "A" and \
          linked_code.lengthRec(dna_seq2) == 1, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 0, 4)
    print(dna_seq2 == None)


def test9():
    """
    Tests duplication function.
    :return: None
    """

    print("Test9: testing duplication")

    dna_seq1 = None
    dna_seq2 = dna.duplication(dna_seq1, 0, 0)
    print(dna_seq2 == None, end=" ")

    try:
        dna_seq2 = dna.duplication(dna_seq1, 0, 1)
        print("False", end=" ")  # failed to catch exception
    except:
        print("True", end=" ")

    dna_seq1 = linked_code.insertAt(0, "A", dna_seq1)
    dna_seq2 = dna.duplication(dna_seq1, 2, 0)
    print(dna_seq2.value == "A" and \
          linked_code.lengthRec(dna_seq2) == 1, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 0, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "A" and \
          linked_code.lengthRec(dna_seq2) == 2, end=" ")

    dna_seq1 = linked_code.insertAt(1, "T", dna_seq1)
    dna_seq1 = linked_code.insertAt(2, "C", dna_seq1)

    dna_seq2 = dna.duplication(dna_seq1, 0, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "A" and \
          linked_code.lengthRec(dna_seq2) == 4, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 1, 1)
    value = dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "T" and \
          linked_code.lengthRec(dna_seq2) == 4
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "T" and \
          linked_code.lengthRec(dna_seq2) == 4, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 2, 1)
    value = dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "C" and \
          dna_seq2.rest.rest.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 4
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "C" and \
          dna_seq2.rest.rest.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 4, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 0, 2)
    value = dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "A" and \
          dna_seq2.rest.rest.rest.value == "T" and \
          dna_seq2.rest.rest.rest.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 5
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "A" and \
          dna_seq2.rest.rest.rest.value == "T" and \
          dna_seq2.rest.rest.rest.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 5, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 1, 2)
    value = dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "C" and \
          dna_seq2.rest.rest.rest.value == "T" and \
          dna_seq2.rest.rest.rest.rest.value == "C"
    print(dna_seq2.value == "A" and \
          dna_seq2.rest.value == "T" and \
          dna_seq2.rest.rest.value == "C" and \
          dna_seq2.rest.rest.rest.value == "T" and \
          dna_seq2.rest.rest.rest.rest.value == "C" and \
          linked_code.lengthRec(dna_seq2) == 5, end=" ")

    try:
        dna_seq2 = dna.duplication(dna_seq1, 2, 2)
        print("False", end=" ")  # failed to catch exception
    except:
        print("True", end=" ")

    print()


def test_all():
    """
    Large test that calls all functions.
    :return: None
    """

    print("Testing all functionality")

    dna_seq1 = dna.convert_to_nodes("ATGCCAATGC")
    dna_seq2 = dna.deletion(dna_seq1, 3, 5)
    dna_seq3 = dna.duplication(dna_seq2, 0, 3)
    dna_seq4 = dna.convert_to_nodes("CC")
    dna_seq5 = dna.insertion(dna_seq3, dna_seq4, 3)
    dna_seq6 = dna.substitution(dna_seq5, 7, "T")
    dna_seq7 = dna.substitution(dna_seq6, 6, "A")

    print(dna.is_match(dna_seq1, dna_seq7), end=" ")

    dna_seq8 = dna.insertion(dna_seq3, dna_seq4, 0)
    dna_seq9 = dna.deletion(dna_seq8, 2, 2)
    dna_seq10 = dna.substitution(dna_seq9, 6, "C")
    dna_seq11 = dna.substitution(dna_seq10, 3, "T")

    print(dna.is_palindrome(dna_seq11), end=" ")

    dna_seq12 = dna.convert_to_nodes("TACG")
    dna_seq13 = dna.duplication(dna_seq12, 0, 4)
    dna_seq14 = dna.duplication(dna_seq13, 3, 1)
    dna_seq15 = dna.duplication(dna_seq14, 5, 1)

    print(dna.is_pairing(dna_seq1, dna_seq15), end=" ")

    print(dna.convert_to_string(dna_seq11) == "CCGTTGCC")


def test_individual():
    """
    Calls individual test functions.
    :return: None
    """

    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()


test_individual()
test_all()
