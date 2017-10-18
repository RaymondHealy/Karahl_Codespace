import sys
import glob
import serial

ser = serial.Serial()

''' 
    Init. Conditions: NA
    Final Conditions: NA

    Parameters: NA

    Returns: A list of all serial ports

    Description: Lists all available serial ports for use with pyserial
    
    Taken from: 
        https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
'''
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

'''
    Init. Conditions: NA
    Final Conditions: NA

    Parameters: s: The string to check

    Returns: A boolean value stating whether 's' is
             a number

    Description: Checks whether or not string 's' is 
                 an integer

    Adapted from:
        http://pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/
'''
def is_unsigned_int(s):
    try:
        value = int(s)
        if value > 0:
            return True
        else:
            return False
    except ValueError:
        return False

'''
    Init. Conditions: An uninitialized object of type Serial() named 'ser'
    Final Conditions: 

    Parameters: NA

    Returns: A boolean value indicating whether or not the serial
             port has been initialized

    Description: Assigns port and baud rate to Serial port 'ser', prompting 
                 the user for both and checking the validity of them (an 
                 available port, and a nonzero, unsigned integer baud)
'''
def startSerial():

    print("----------Starting The Serial Ports----------")
    print("  Checking the available serial ports")
    portList = serial_ports()

    printListResponse = input('Do you need a list of Com Ports? Y/N:')
    if printListResponse[0] == 'y' or printListResponse[0] == 'Y':
        for element in portList:
            print(element)

    validPort = False
    while not validPort:
        userPort = input("Port Name (type 'Exit' to shut down): ")
        if userPort == 'Exit':
            return False
            break

        for element in portList:
            if element == userPort:
                validPort = True
                ser.port = userPort
                break

    validBaud = False
    while not validBaud:
        userBaud = input("Baud Rate (type '0' or 'Exit' to shut down): ")
        if not is_unsigned_int(userBaud) and userBaud == 'Exit':
            return False
        elif int(userBaud) == 0:
            return False
        else:
            ser.baudrate = int(userBaud)
            validBaud = True
    ser.timeout = 1
    if not ser.is_open:
        ser.open()
        print("  Serial Port Open")
    print('---------------------------------------------')
    return True

def main():
    '''
    if startSerial():
        while True:
            print(ser.readline())'''
    ser.baudrate = 9600
    ser.port = 'COM6'
    ser.timeout = 1
    ser.open()
    while True:
        toPrint = str(ser.readline())
        if toPrint[:2] == "b'":
            toPrint = toPrint[2:-3]

        print(toPrint)

main()