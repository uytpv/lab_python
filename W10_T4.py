########################################################
# Task: W10_T4
# Developer: UY TRA
# Description:
# Create program which is able to read timestamp from a file.
# Timestamp in this context means that there are two fields,
# Datetime field and Value field.
# Data: W10_T4D1.txt
#########################################################

import W10_T4Lib as Time
timeStamp = []


def menu():
    print('Choose operation:')
    print('1 - Show current date and time in ISO format')
    print('2 - Read timestamp from file')
    print('3 - Print timestamp')
    print('0 - Exit')
    choice = int(input('Your choice: '))
    if choice == 1:
        Time.showCurrentIsoFormat()
        menu()
    elif choice == 2:
        global timeStamp
        timeStamp = Time.readTimestampFromFile()
        menu()
    elif choice == 3:
        Time.printTimestamp(timeStamp)
        menu()
    elif choice == 0:
        print('Exiting.')
        print()
        print('Thank you for using the program.')
    else:
        print('Unknown option, try again.')
        print()
        menu()

    return None


print('Welcome to the program.')
menu()
