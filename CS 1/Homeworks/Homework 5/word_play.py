"""Raymond Healy"""

""" Init. Conditions:NA
    Final Conditions:NA

    Parameters: word: the string to check for against the list
                fileRef: a reference to an opened file
    
    Returns: The number of words found in the file by deleting
             individual characters from the word parameter
             (prints each deletion word in the order it is found)

    Description: plays the "deletion" game with the word, 
                 removing each letter from it and checking
                 it against the "fileRef" list
    """
def check_deletion(word, fileRef):
    numMatches = 0
    lastChar = ''
    for line in fileRef:
        line = line.strip()
        charIndex = 0
        if len(line) == len(word) -1:
            for char in word:
                if not lastChar == char:
                    if charIndex == 0:
                        checkString = word[1:]
                    elif charIndex == len(word) - 1:
                        checkString = word[:len(word)-1]
                    else:
                        checkString = word [:charIndex] + word[charIndex+ 1:]

                    if line == checkString:
                        numMatches += 1
                        print(numMatches, " ", line)
                lastChar = char
                charIndex += 1
    return numMatches

""" Init. Conditions: NA
    Final Conditions: NA

    Parameters: NA

    Returns: NA (prints the number of deletion words returned)

    Description: Runs the deletion game function, prompting the
                 user for the word and the file
"""
def main():
    gotWord = False
    while not gotWord:
        word = input("Enter a word you want to check: ")
        if word == '' or word == ' ' or word == '\n' or word == '\t':
            print("Enter a valid word")
            gotWord = False
            continue
        else:
            gotWord = True

    gotFile = False
    while not gotFile:
        file = input("Enter the name of the text file to check: ")
        if file == '' or word == ' ' or word == '\n' or word == '\t':
            print("Enter a valid file")
            gotFile = False
            continue
        else:
            gotFile = True


    fileRef = open(file)
    print(check_deletion(word, fileRef), " deletion word(s) found")

main()
