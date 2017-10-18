"""Raymond Healy"""

def kEncodingFactor():
    return 11

def muddle(fileRef):
    strEnc = ''
    fileRef.seek(0)
    for line in fileRef:
        for char in line:
            strEnc += chr(ord(char) + kEncodingFactor())
    return strEnc

def clarify(fileRef):
    strEnc = ''
    fileRef.seek(0)
    for line in fileRef:
        for char in line:
            strEnc += chr(ord(char) - kEncodingFactor())
    return strEnc

def isMuddled(filePath):
    return filePath.strip()[-4:] == ".mud"

def isText(filePath):
    return filePath.strip()[-4:] == ".txt"

def main():
    filePath = input("Enter the file path to decode or encode: ")
    while not filePath.strip() == '':
        if isText(filePath):
            fr = open(filePath, 'r', encoding='utf8')
            output = muddle(fr)

            if input("type 'y' to save to "+ filePath[:len(filePath)-4]+ ".mud: ") == 'y':
                fr2 = open(filePath[:len(filePath)-4] + ".mud", 'w', encoding='utf8')
                fr2.write(output)
                fr2.close()
            else:
                print(output)

            fr.close()
            break
        elif isMuddled(filePath):
            fr = open(filePath, 'r', encoding='utf8')
            output = clarify(fr)

            if input("type 'y' to save to "+ filePath[:len(filePath)-4]+ "2.txt: ") == 'y':
                fr2 = open(filePath[:len(filePath)-4] + "2.txt", 'w', encoding = 'utf8')
                fr2.write(output)
                fr2.close()
            else:
                print(output)

            fr.close()
            break
        else:
            print("valid file extensions are '.txt' and '.mud'")

        filePath = input("Enter the file path to decode or encode: ")

main()