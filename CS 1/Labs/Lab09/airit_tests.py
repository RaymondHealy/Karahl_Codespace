from airit_simulation import *


def test_read_passenger():
    print("\nTesting <<PassengerFromFile()>> :")
    with open('Files/passengers_very_small.txt') as f:
        passenger = PassengerFromFile(f)
        print("\tPassengers:")
        while passenger is not None:
            print('\t\t',passenger)
            passenger = PassengerFromFile(f)
        f.close()


def test_line_up():
    print("\nTesting <<line_up()>> :")
    with open('Files/passengers_very_small.txt') as f:
        gate = mkEmptyGate(8)
        allStudentsQueued = line_up(gate, f)
        print("\tQueues:")
        for line in gate.queues:
            print('\t\t', line, end="\n")



        if allStudentsQueued:
            print('\tAll Students Have Been Queued')
        else:
            print("\tUnqueued Passengers:")
            for line in f:
                print('\t\t',line.strip())

        f.close()


def main():
    test_read_passenger()
    test_line_up()


if __name__ == '__main__':
    main()
