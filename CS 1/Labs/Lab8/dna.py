from linked_code import *

"""----------------------------<Required Functions>----------------------------"""
def convert_to_nodes(dna_string):
    dna_string = dna_string.strip()
    if dna_string == '':
        return None
    else:
        return Node(dna_string[0].upper(), convert_to_nodes(dna_string[1:]))

def convert_to_string(dna_seq):
    if dna_seq == None:
        return ''
    else:
        return dna_seq.value + convert_to_string(dna_seq.rest)

"""Returns a bool indicating whether or not the 2 sequences are identical"""
def is_match(dna_seq1, dna_seq2):
    if dna_seq1 == None == dna_seq2:
        return True
    elif dna_seq1 == None or dna_seq2 == None:
        return False
    elif dna_seq1.value != dna_seq2.value:
        return False
    else:
        return is_match(dna_seq1.rest, dna_seq2.rest)

"""Returns a boolean value indicating wether or not the 2 sequences are valid pair sequences"""
def is_pairing(dna_seq1, dna_seq2):
    if dna_seq1 == None == dna_seq2:
        return True
    elif dna_seq1 == None or dna_seq2 == None:
        return False
    elif not IsValidPair(dna_seq1.value, dna_seq2.value):
        return False
    else:
        return is_pairing(dna_seq1.rest, dna_seq2.rest)

"""Returns a boolean value indicating whether or not the sequence is palindromic"""
def is_palindrome(dna_seq):
    return is_match(dna_seq, reverseTailRec(dna_seq))

"""Replaces value at idx with base recursively and non-destructively"""
def substitution(dna_seq, idx, base):
    if dna_seq == None:
        raise IndexError("Sequence Index Out of Range")
    if idx > 0:
        return Node(dna_seq.value, substitution(dna_seq.rest, idx - 1, base))
    else:
        return Node(base.upper(), dna_seq.rest)

"""Inserts <<dna_seq2>> at index <<idx>> in <<dna_seq>>"""
def insertion(dna_seq1, dna_seq2, idx):
    if idx == 0:
        return cat(dna_seq2, dna_seq1)
    elif dna_seq1 == None:
        raise IndexError("Sequence Index Out of Range")
    else:
        return Node(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, idx - 1))

        
""" <<segment_size>> characters from <<dna_seq>> starting with index <<idx>>"""
def deletion(dna_seq, idx, segment_size):
    if segment_size == 0:
        return dna_seq
    elif dna_seq == None:
        raise IndexError("Sequence Index Out of Range")
    elif idx > 0:
        return Node(dna_seq.value, deletion(dna_seq.rest, idx - 1, segment_size))
    else:
        return deletion(dna_seq.rest, 0, segment_size - 1)

def duplication(dna_seq, idx, segment_size):
    if segment_size == 0:
        return dna_seq
    elif dna_seq is None:
        raise IndexError("Sequence Index Out of Range")
    elif idx > 0:
        return Node(dna_seq.value, duplication(dna_seq.rest, idx - 1, segment_size))
    elif segment_size > 0:
        temp = insertAt(segment_size - idx, dna_seq.value, dna_seq)
        if segment_size -1 > 0:
            return Node(dna_seq.value, duplication(temp.rest, idx - 1, segment_size - 1))
        else:
            return Node(dna_seq.value, temp.rest)
"""----------------------------------------------------------------------------"""

"""-----------------------------<Helper Functions>-----------------------------"""
def IsValidPair(char1, char2):
    char1 = char1.strip()[0].upper()
    char2 = char2.strip()[0].upper()
    if char1 == 'G' and char2 == 'C':
        return True
    elif char1 == 'C' and char2 == 'G':
        return True
    elif char1 == 'T' and char2 == 'A':
        return True
    elif char1 == 'A' and char2 == 'T':
        return True
    else:
        return False
"""----------------------------------------------------------------------------"""
