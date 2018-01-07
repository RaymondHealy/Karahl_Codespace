from rit_lib import *

"""Raymond Healy"""

"""
<true> is the <1> side, <false> is the <0> side
"""
Trie = struct_type("Trie", (("Trie", str, NoneType), "true"), (("Trie", str, NoneType), "false"))


def MkTrie(true=None, false=None):
    """Make a Trie with the provided values"""
    return Trie(true, false)


"""--------------------------------<Required Functions>-------------------------------"""


def Insert(trie, string):
    """Insert binary string <<string>> into the proper place in trie <<trie>>"""
    if trie is None:  # If <<trie>> is a None
        return string  # Just hand back the String

    if isinstance(trie, str):  # If the given trie is a string
        trie = trie.strip()  # Strip string <<trie>>
        if trie[0] == '1':  # If the first character of <<trie>> is a <<'1'>>
            trie = MkTrie(trie, None)  # Set <<trie>> to a <<Trie>> with <<trie>> on the <<true>> branch
        else:  # Otherwise (if the first character of <<trie>> is a <<'0'>>)
            trie = MkTrie(None, Trie)  # Set <<trie>> to a <<Trie>> with <<trie>> on the <<false>> branch

    if isinstance(trie, Trie):  # If <<trie>> is a <<Trie>> class object
        return InsertRec(trie, string.strip(), 0)  # Start recursion to place the stripped <<string>> of <<trie>>


def Trie2List(trie):
    if not isinstance(trie, Trie):
        return [trie]
    else:
        lowList = Trie2List(trie.false)
        highList = Trie2List(trie.true)
        if lowList[0] is None and highList[0] is None:
            return [None]
        elif lowList[0] is None:
            return highList
        elif highList[0] is None:
            return lowList
        else:
            return lowList + highList


def Largest(trie):
    if trie is None:
        return None
    elif isinstance(trie, str):
        return trie
    elif trie.true is None:
        return Largest(trie.false)
    else:
        return Largest(trie.true)


def Smallest(trie):
    if Trie is None:
        return None
    elif isinstance(trie, str):
        return trie
    elif trie.false is None:
        return Smallest(trie.true)
    else:
        return Smallest(trie.false)


def Search(trie, string):
    """
    Init. Conditions:   - <<trie>> must not be empty. it must have at least 1 binary entry
                        - <<string>> must be composed only of "0"s and "1"s

    Final Conditions:   Nope

    Parameters: trie:   A trie-type tree, with <<true>> (1) and <<false>> (0) branches
                string: A string of binary numerals, used to

    Returns:

    Description:
"""
    string = string.strip()
    if not isinstance(trie, Trie):
        return trie
    else:
        return SearchRec(trie, string)


def Split(string1, string2, idx):
    """
    Init. Conditions:   - A non-empty <<Trie>> type object, <<trie>>
                        - 2 strings (<<string1>> and <<string2>>) which conflict at index <<idx>>

    Final Conditions:   NA

    Parameters: string1:    Conflicting string 1 (generally the new string)
                string2:    Conflicting string 2 (generally the pre-existing string)
                idx:        The depth in the tree and the index of the conflicting character

    Returns:    - A new object of type <<Trie>> which can be put in the place of the original leaf node
                  and has all needed branches to distinguish <<string1>> and <<string2>>
                - **OR** The original string, iff the strings match

    Description: Takes 2 strings (<<string1>> and <<string2>>) of binary digits which conflict at index <<idx>>
                 and returns either the string if the 2 don't match or a <<Trie>> with all of the branbches
                 needed to differentiate the two.
    """
    if string1 == string2:  # If the 2 strings don't conflict
        return string1
        # Just return the damn thing as a string
    elif string1[idx] == string2[idx]:  # Otherwise if the strings match at index <<idx>>
        if string1[idx] == '1':  # If they are positive at the specified index
            return MkTrie(Split(string1, string2, idx + 1), None)
            # Return a new <<Trike>> with the properly branched strings coming off of the <<true>> branch
        else:  # Otherwise (If both are negative at the specified index)
            return MkTrie(None, Split(string1, string2, idx + 1))
            # Return a new <<Trike>> with the properly branched strings coming off of the <<false>> branch
    elif string1[idx] == '1':  # Otherwise (if differing) if <<string1>> is a <<'1'>> character
        return MkTrie(string1, string2)
        # Return a new <<Trie>> with <<string1>> on the <<true>> branch and <<string2>> on the <<false>> branch
    else:  # Otherwise (if <<string1>> != <<string2>> and <<string1>> is a <<'0'>> character
        return MkTrie(string2, string1)
        # Return a new <<Trie>> with <<string2>> on the <<true>> branch and <<string1>> on the <<false>> branch


def Size(trie):
    return len(Trie2List(trie))


def Height(trie):
    if isinstance(trie, Trie):
        return HeightRec(trie)
    else:
        return 1


"""-----------------------------------------------------------------------------------"""

"""-------------------------------<Recursion Functions>-------------------------------"""


def SearchRec(trie, string, idx=0):
    """
        Init. Conditions:   - <<trie>> must be either a <<str>> of binary digits or a non-empty <<Trie>>
                            - <<string>> must be a <<str>> type object composed entirely of binary digits
                            - <<idx>> must be a valid integer index of <<string>>
                            - <<preferHigh>> must be either a boolean value or a <<None>>

        Final Conditions:   NA

        Parameters: trie        - An object of class <<Trie>> or <<str>>
                    string      - A <<str>> of binary digits (<<'0'>>s and <<'1'>>s)
                    idx         - A valid <<int>> index of <<str>>, indicating the digit to check
                    preferHigh  - Either a boolean (<<True>>/<<False>>) value or a <<None>>
                                - If <<None>>, continue folowing the branches as indicated by character <<string[idx]>>
                                - If <<True>>, take the <<true>> branch of <<trie>> whenever possible until
                                  reaching a leaf
                                - If <<False>>, take the <<false>> branch of <<trie>> whenever possible until
                                  reachina a leaf

        Returns: The <<str>> of binary digits in <<trie>> closest in value to the value of binary digits in <<string>>

        Description: Searches <<trie>> for the closest number represented by the <<str>> of binary digits <<string>>
                     already in <<trie>>. If the path specified has not been terminated by a null node (a <<None>>),
                     it follows the path through <<trie>> indicated by <<string>>, chosing branches based on the
                     digit at index <<idx>>. If a perfect match is found, it returns said match. Otherwise (if the
                     specified path ends in a <<None>>), the value of expression <<string[index] == '1'>> is saved to
                     <<preferHigh>> for further recursive calls, and the indicated path is followed (when possible)
                     until reaching a leaf ( a <<str>>)
    """
    if isinstance(trie, str):  # If passed a leaf node
        return trie  # Return the leaf (closest match)
    else:
        if string[idx] == '1':  # If we should follow the <<true>> branch
            if trie.true is None:  # If the <<true>> branch is a null node
                return Largest(trie.false)
                # Recursive call looking down the valid <<false>> branch, taking <<true>> branches
                # whenever possible to find the closest matching leaf node
            else:  # Otherwise, if <<string>> specifies a valid path through <<trie>>
                return SearchRec(trie.true, string, idx + 1)
                # Recursive call down the <<true>> branch, looking at the next character in <<string>>
        else:  # Otherwise (if we should follow the <<false>> branch)
            if trie.false is None:  # If the <<false>> branch is a null node
                return Smallest(trie.true)
                # Recursive call looking down the valid <<true>> branch, taking <<false>> branches
                # whenever possible to find the closest matching leaf node
            else:  # Otherwise, if <<string>> specifies a valid path through <<trie>>
                return SearchRec(trie.false, string, idx + 1)
                # Recursive call down the <<false>> branch, looking at the next character in <<string>>


def InsertRec(trie, string, idx):
    """
    Insert a binary string <<string>> into proper place in trie <<trie>>.

    Called by <<Insert(trie, string)>>. checks string index <<layer>>
    for sorting purposes
    """
    """-----------------------------<Check String Length>-----------------------------"""
    if idx + 1 > len(string):
        """Custom index error message"""
        raise IndexError("Invalid String Index. Non-terminating Recursion in <<InsertRec(trie, string, layer)>>")

    """----------------------<Determine which branch to go for>-----------------------"""
    if string[idx] == '1':  # If on the <<true>> branch
        if trie.true is None:  # If the branch is empty
            trie.true = string  # Set the end of the <<true>> branch to a leaf with value <<string>>
            return True
        else:  # Otherwise (if branch is not empty)
            if isinstance(trie.true, Trie):
                return InsertRec(trie.true, string, idx + 1)
            else:
                trie.true = Split(trie.true, string, idx + 1)
                return True

    else:  # Otherwise (if on the <<false>> branch)
        if trie.false is None:  # If the branch is empty
            trie.false = string  # Set the end of the <<false>> branch to a leaf with value <<string>>
        else:  # Otherwise (if the branch is not empty)
            if isinstance(trie.false, Trie):
                return InsertRec(trie.false, string, idx + 1)
            else:
                trie.false = Split(trie.false, string, idx + 1)
                return True


def HeightRec(trie, depth=1):
    if (trie.true is None or isinstance(trie.true, str)) and (trie.false is None or isinstance(trie.false, str)):
        return depth
    elif trie.true is None or isinstance(trie.true, str):
        return HeightRec(trie.false, depth + 1)
    elif trie.false is None or isinstance(trie.false, str):
        return HeightRec(trie.true, depth + 1)
    else:
        trueDepth = HeightRec(trie.true, depth + 1)
        falseDepth = HeightRec(trie.true, depth + 1)
        if trueDepth >= falseDepth:
            return trueDepth
        else:
            return falseDepth


"""-----------------------------------------------------------------------------------"""

"""--------------------------------<Helper Functions>---------------------------------"""


def PrintTrie(trie, numTabs=0):
    if not isinstance(trie, Trie):
        Indent(numTabs)
        print(trie)
    else:
        Indent(numTabs)
        print("False:")
        PrintTrie(trie.false, numTabs + 2)
        Indent(numTabs)
        print("True:")
        PrintTrie(trie.true, numTabs + 2)


def List2Trie(lstStrings):
    trie = MkTrie()

    for string in lstStrings:
        Insert(trie, string.strip())
    return trie


def Indent(numTabs):
    for i in range(numTabs):
        print('\t', end='')


"""-----------------------------------------------------------------------------------"""

"""-----------------------------<Prefered Syntax Matching>----------------------------"""


def insert(trie, st):
    return Insert(trie, st)


def search(T, x):
    """
    The prefered syntax for the search function. just passes through <<T>>,
    a <<Trie>> and <<x>> a string of binary characters ("1"s and "0"s) to
    search for.
    """
    return Search(T, x)


def split(x, y, idx):
    return Split(x, y, idx)


def trie_to_list(trie):
    return Trie2List(trie)


def largest(trie):
    return Largest(trie)


def smallest(trie):
    return Smallest(trie)


def size(trie):
    return Size(trie)


def height(trie):
    return Height(trie)


"""-----------------------------------------------------------------------------------"""

"""---------------------------------<Test Functions>----------------------------------"""


def TestInsert(lstStrings=["001010", "000111", "111000", "010000", "110001"]):
    newEntry = lstStrings[0].strip()
    lstStrings = lstStrings[1:]

    trie = MkTrie()
    if newEntry[0] == '1':
        trie = MkTrie(newEntry, None)
    else:
        trie = MkTrie(None, newEntry)

    for string in lstStrings:
        Insert(trie, string)

    PrintTrie(trie)


def TestSplit(string1="001010", string2="000111"):
    PrintTrie(split(string1, string2, 0))


def TestTrie2List(lstStrings=["001010", "000111", "111000", "010000", "110001"]):
    trie = List2Trie(lstStrings)
    lst = trie_to_list(trie)

    lstStrings.sort()
    print(lst == lstStrings)


def TestLargest(lstStrings=["001010", "000111", "111000", "010000", "110001"]):
    trie = List2Trie(lstStrings)
    checkLargest = lstStrings[0].strip()
    lstStrings = lstStrings[1:]
    for string in lstStrings:
        if int(string.strip()) > int(checkLargest):
            checkLargest = string.strip()

    print(Largest(trie) == checkLargest)


def TestSearch(lstStrings=["001010", "000111", "111000", "010000", "110001"], string="100010"):
    trie = List2Trie(lstStrings)

    dif = abs(int(lstStrings[0]) - int(string))
    match = lstStrings[0]
    lstStrings = lstStrings[1:]
    for i in lstStrings:
        if abs(int(i) - int(string)) < dif:
            match = i

    print(SearchRec(trie, string, 0) == match)


def TestSmallest(lstStrings=["001010", "000111", "111000", "010000", "110001"]):
    trie = List2Trie(lstStrings)
    checkSmallest = lstStrings[0].strip()
    lstStrings = lstStrings[1:]
    for string in lstStrings:
        if int(string.strip()) < int(checkSmallest):
            checkSmallest = string.strip()

    print(Smallest(trie) == checkSmallest)


def TestSize(lstStrings=["001010", "000111", "111000", "010000", "110001"]):
    result = Size(List2Trie(lstStrings))
    print(result == len(lstStrings))


def TestHeight(lstStrings=["001010", "000111", "111000", "010000", "110001"]):
    print(Height(List2Trie(lstStrings)))


"""-----------------------------------------------------------------------------------"""


def Main():
    print("--------------------------Testing Insert--------------------------")
    TestInsert()
    print("\n--------------------------Testing Trie2List--------------------------")
    TestTrie2List()
    print("\n--------------------------Testing Search--------------------------")
    TestSearch()
    print("\n--------------------------Testing Largest--------------------------")
    TestLargest()
    print("\n--------------------------Testing Split--------------------------")
    TestSplit()
    print("\n--------------------------Testing Height--------------------------")
    TestHeight()
    print("\n--------------------------Testing Size--------------------------")
    TestSize()
    print("\n--------------------------Testing Smallest--------------------------")
    TestSmallest()


if __name__ == '__main__':
    Main()
