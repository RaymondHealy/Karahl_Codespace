
def readFile(filename):
    logLines = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            (timeChunk, line) = GetNextDataChunk(line)
            (time, timeStamp) = GetTimestamp(timeChunk)
            (eventChunk, line) = GetNextDataChunk(line)

            if line is None:
                logLines += [{'timeStamp': timeStamp, 'time': time, 'event': eventChunk[9:-1], 'remainder': ''}]
            else:
                logLines += [{'timeStamp': timeStamp, 'time': time, 'event': eventChunk[9:-1], 'remainder': line.strip(" }\n\t\r")}]

    return logLines


def WriteLogToFile(filename, lst):
    with open(filename, 'w', encoding='utf8') as f:
        for entry in lst:
            f.write(str(entry) + '\n')


def WriteEventsToFile(lst, includeRemainder=False, maxRemaindersToPrint = 0, filename = 'Output.txt'):
    maxRemaindersToPrint = abs(int(maxRemaindersToPrint))

    # If we should include the remainders
    with open(filename, 'w', encoding='utf8') as f:
        if includeRemainder:
            # The dictionary to hold the event key and remainder lists
            eventLst = {}

            # For dictionary in the list from the readFile
            for dictionary in lst:
                # The key will be the event from the dictionary
                event = dictionary['event']
                # What is left of the string after extracting the event and the timestamp
                remainder = dictionary['remainder']

                if not event in eventLst:
                    # If the key isn't set yet, start the remainder list
                    eventLst[event] = [remainder]
                else:
                    # Otherwise, append this remainder to the list
                    if maxRemaindersToPrint:
                        if len(eventLst[event]) < maxRemaindersToPrint:
                            eventLst[event] += [remainder]
                    else:
                        eventLst[event] += [remainder]


            # For Each event type
            for key in eventLst:
                # Write out the key and add in a new line
                f.write(str(key) + ':' + '\n')

                # For each Remainder in the list
                for entry in eventLst[key]:
                    # Remove the whitespace and the hanging close bracket
                    # Write the entry to the file, indented and with a line between each entry
                    f.write('\t' + entry + '\n\n')

                f.write("\n\n")
        else:
            eventLst = []
            for dictionary in lst:
                event = dictionary['event']
                if not event in eventLst:
                    eventLst += [event]

            eventLst.sort(key=str.lower)
            for entry in eventLst:
                f.write(entry + '\n')
"""----------------------------------<PARSE_STRINGS>----------------------------------"""


def GetTimestamp(logLineStr):
    toReturn = {}  # Create the dictionary to return
    timeStamp = logLineStr[15:34]  # Extract the timestamp from the string
    timeStamp = timeStamp.split('T')  # Split the date and time

    # Separate the date and time
    date = timeStamp[0]
    time = timeStamp[1]

    # Split up the time stamp into a dictionary.
    date = date.split('-')
    time = time.split(':')
    toReturn['year'] = int(date[0])
    toReturn['month'] = int(date[1])
    toReturn['day'] = int(date[2])
    toReturn['hour'] = int(time[0])
    toReturn['minute'] = int(time[1])
    toReturn['second'] = int(time[2])

    timeStamp = toReturn['year'] * 10 ** 10 + toReturn['month'] * 10 ** 8 + toReturn['day'] * 10 ** 6
    timeStamp += toReturn['hour'] * 10 ** 4 + toReturn['minute'] * 10 ** 2 + toReturn['second']

    return toReturn, timeStamp


def GetNextDataChunk(string):
    toReturn = ''
    for ch in string:
        if ch == ',':
            return toReturn.strip(), string[len(toReturn):].strip(' ,\n\r\t')
        else:
            toReturn += ch
    return toReturn.strip(), ''


"""--------------------------------<END_PARSE_STRINGS>--------------------------------"""


def main():
    lst  = readFile("Journals\Old\Journal.170608090204.01.log")
    lst += readFile("Journals\Old\Journal.170608172616.01.log")
    lst += readFile("Journals\Old\Journal.170609123909.01.log")
    lst += readFile("Journals\Old\Journal.170609153821.01.log")
    lst += readFile("Journals\Old\Journal.170609170123.01.log")
    lst += readFile("Journals\Old\Journal.170609193333.01.log")
    lst += readFile("Journals\Old\Journal.170609195431.01.log")
    lst += readFile("Journals\Old\Journal.170610080647.01.log")
    lst += readFile("Journals\Old\Journal.170611142629.01.log")
    lst += readFile("Journals\Old\Journal.170611174809.01.log")
    lst += readFile("Journals\Old\Journal.170612105133.01.log")
    lst += readFile("Journals\Old\Journal.170612152610.01.log")
    lst += readFile("Journals\Old\Journal.170613091640.01.log")
    lst += readFile("Journals\Old\Journal.170613153230.01.log")
    lst += readFile("Journals\Old\Journal.170613191732.01.log")
    lst += readFile("Journals\Old\Journal.170613193357.01.log")
    lst += readFile("Journals\Old\Journal.170615112817.01.log")
    lst += readFile("Journals\Old\Journal.170615142257.01.log")
    lst += readFile("Journals\Old\Journal.170616135632.01.log")
    lst += readFile("Journals\Old\Journal.171105150721.01.log")
    lst += readFile("Journals\Journal.171107161638.01.log")

    eventLst = []
    for element in lst:
        event = element['event']
        remainder = element['remainder']


        if event == 'SendText' or event == 'ReceiveText':
            Extra = remainder.strip()[:]
            print(Extra)
            if remainder.strip()[-5:] != '':
                eventLst += [element]

    WriteEventsToFile(eventLst, True)

main()
