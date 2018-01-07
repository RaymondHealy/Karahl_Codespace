from rit_lib import *
from myQueue import *
from myStack import *

# //------------------------------------------------------------------------------------------------------//

Passenger = struct_type("Passenger", (str, "name"), (int, "number"), (bool, "carryOn"))

def PassengerFromFile(fr):
    passData = fr.readline().strip()
    if passData == "":
        return None
    else:
        passData = passData.split(',')
        return Passenger(passData[0].strip(), int(passData[1].strip()), "TRUE" == passData[2].strip().upper())

# //------------------------------------------------------------------------------------------------------//
Gate = struct_type("Gate", (list, "queues"), (int, "maxCapacity"), (int, "currentPassengers"))

def mkEmptyGate(maxCapacity, numQueues=4):
    gate = Gate([], maxCapacity, 0)
    for i in range(0, numQueues):
        gate.queues += [mkEmptyQueue()]
    return gate

def GateEmpty(gate):
    isEmpty = True
    for queue in gate.queues:
        queueEmpty = emptyQueue(queue)
        isEmpty = isEmpty and queueEmpty
    return isEmpty

def DequeueNextPassenger(gate):
    nextPassenger = None
    if not GateEmpty(gate):

        for i in range(len(gate.queues) - 1, -1, -1):
            queue = gate.queues[i]
            if nextPassenger is None and not emptyQueue(queue):
                nextPassenger = front(queue)
                dequeue(queue)
                gate.currentPassengers -= 1
                break

    return nextPassenger

def EnqueuePassenger(passenger, gate):
    if gate.currentPassengers >= gate.maxCapacity:
        return passenger
    else:
        queue = int(str(passenger.number)[0]) - 1
        enqueue(gate.queues[queue], passenger)
        gate.currentPassengers += 1
# //------------------------------------------------------------------------------------------------------//
Plane = struct_type("Plane", (Stack, "CarryOn"), (Stack, "NoCarryOn"),
                    (int, "MaxCapacity"), (int, "CurrentPassengers"))

def mkEmptyPlane(maxCap):
    return Plane(mkEmptyStack(), mkEmptyStack(), maxCap, 0)

def RoomOnPlane(plane):
    return plane.MaxCapacity > plane.CurrentPassengers

def EmptyPlane (plane):
    return emptyStack(plane.CarryOn) and emptyStack(plane.NoCarryOn)

def BoardPassenger(passenger, plane):
    if RoomOnPlane(plane) and passenger is not None:
        if passenger.carryOn:
            push(plane.CarryOn, passenger)
        else:
            push(plane.NoCarryOn, passenger)

        plane.CurrentPassengers += 1
        return True

    else:
        return False

def UnboardPassenger(plane):
    if not emptyStack(plane.NoCarryOn):
        passenger = top(plane.NoCarryOn)
        pop(plane.NoCarryOn)
        plane.CurrentPassengers -= 1
        return passenger
    elif not emptyStack(plane.CarryOn):
        passenger = top(plane.CarryOn)
        pop(plane.CarryOn)
        plane.CurrentPassengers -= 1

        return passenger
    else:
        return None
# //------------------------------------------------------------------------------------------------------//
def line_up(gate, file):
    allStudentsQueued = False

    print("\nPassengers Are Queueing:")
    if gate.currentPassengers < gate.maxCapacity:
        nextPassenger = PassengerFromFile(file)
        if nextPassenger is not None:

            print("\t", nextPassenger)
            EnqueuePassenger(nextPassenger, gate)
        else:
            print("No Students Left To Queue")

    while gate.currentPassengers < gate.maxCapacity and nextPassenger is not None:
        nextPassenger = PassengerFromFile(file)
        if nextPassenger is not None:
            print("\t", nextPassenger)
            EnqueuePassenger(nextPassenger, gate)

        else:
            print("No Students Remaining To Queue")

    if gate.currentPassengers >= gate.maxCapacity:
        return True
    else:
        return False


def BoardPlane (plane, gate):
    print("\nPassengers Are Boarding The Plane:")
    boardedPassengers = False
    while RoomOnPlane(plane) and not GateEmpty(gate):
        boardedPassengers = True
        nextPassenger = DequeueNextPassenger(gate)
        if nextPassenger is not None:
            print('\t', nextPassenger)
            BoardPassenger(nextPassenger, plane)

    if not RoomOnPlane(plane):
        print("The Plane Is Full, Taking Off")
        return False
    else:
        print("The Gate is Empty", end = ' ')
        if boardedPassengers:
            print(', taking off')
        else:
            print('')
        return True

def UnboardPlane (plane):
    print("\nPassengers Are Dissembarking:")
    while not EmptyPlane(plane):
        print('\t', UnboardPassenger(plane))



# //------------------------------------------------------------------------------------------------------//

def main():
    fileName = input("Passenger File Path (default to very small file): ").strip()
    if fileName == "":
        fileName = "Files\passengers_very_small.txt"

    gateCap = input("Max Capacity At The Gate: ").strip()
    if gateCap == "":
        gateCap = 8
    else:
        gateCap = int(gateCap)

    planeCap = input("Max Capacity On The Plane: ").strip()
    if planeCap == "":
        planeCap = 5
    else:
        planeCap = int(gateCap)

    gate = mkEmptyGate(gateCap)
    plane = mkEmptyPlane(planeCap)

    with open(fileName) as f:
        waiting = not line_up(gate, f)
        while waiting:
            BoardPlane(plane, gate)

            while not GateEmpty(gate):
                UnboardPlane(plane)
                BoardPlane(plane, gate)

            waiting = line_up(gate, f)
        while not GateEmpty(gate):
            UnboardPlane(plane)
            BoardPlane(plane, gate)






if __name__ == '__main__':
    main()
