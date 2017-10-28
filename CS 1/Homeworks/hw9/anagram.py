"""Raymond Healy"""
"""
Provided Dictionary is 'american-english.txt'
"""

from quickSort import *


"""-------------------------------<Utilities>-------------------------------"""
"""
Utility:
    Takes a string and sorts its characters alphabetically
Returns the sorted string of lowercase characters
"""
def SortString (str):
    temp = []
    for ch in str:
        temp += [ch.lower()]

    temp.sort()


    output = ''
    for ch in temp:
        output = output + ch
    return output

def PrintHelp():
    print("Commands:\n",
          "    2   : Get a list of anagrams from a string\n",
          "    3   : Get the maximum number of anagrams of\n"
          "          a user-specified word length\n",
          "    4   : Get the number of no anagram words of\n",
          "          a user-specified word length\n",
          "  Help  : View this list again\n",
          "  Exit  : Leave the function")
"""-------------------------------------------------------------------------"""

"""----------------------------<Homework Tasks>-----------------------------"""
"""
Task 1 of the homework:
    Creates a dictionary based off of the given file, with one word 
per line. The keys are the word's letters alphabetized and 
in lower case.
"""
def CreateDictionary (filename):
    anagrams = {}
    with open(filename) as f:
        for line in f:
            key = SortString(line.strip())
            if key in anagrams:
                anagrams[key] += [line.strip()]
            else:
                anagrams[key] = [line.strip()]

    return anagrams

"""
Task 2 of homework:
    Get all anagrams for words given a string
"""
def GetAnagrams (str, anagramDictionary):
    key = SortString(str)
    if key in anagramDictionary:
        return anagramDictionary[key]
    else:
        return None

"""
Task 3 of Homework:
    Takes a positive, non-zero word length and returns 
the size of the largest list of anagrams that length
"""
def MaxListOfWordLength (length, dictionary):
    maxLength = 0
    for key in dictionary:
        if len(key) == length and len(dictionary[key]) > maxLength:
            maxLength = len(dictionary[key])
    return maxLength

"""
Task 4 of Homework:
    Gives the number of words without anagrams of a 
given length in a dictionary of anagrams
"""
def NumGoodJumbleWords (wordLength, dictionary):
    numJumbles = 0
    for key in dictionary:
        if len(key) == wordLength and len(dictionary[key] == 1):
            numJumbles+= 1
    return numJumbles
"""-------------------------------------------------------------------------"""

"""
Final Implementations
"""
def main ():
    anagramDict = CreateDictionary('american-english.txt')
    PrintHelp()
    while True:
        choice = input("\nEnter Your Command (Type Help for a List): ").strip().lower()
        print('')
        if choice == '2':
            #Task 2
           print(GetAnagrams(input('What Would you Like to Get Anagrams Of? '),
                             anagramDict))
        elif choice == '3':
            #Task 3
            print(MaxListOfWordLength(int(input("Enter the Length of Words to Check: ")),
                                      anagramDict))
        elif choice == '4':
            #Task 4
            print(NumGoodJumbleWords(int(input("What Word Length Would you Like to Search For? ")),
                                     anagramDict))
        elif choice == 'help':
            PrintHelp()
            #Print the Requested Assistance
        elif choice == 'exit':
            #Break out of the loop
            break
        else:
            #no valid option chosen
            print("***INVALID OPTION*** Enter Help for a list of valid commands")

main()