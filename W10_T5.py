########################################################
# Task: W10_T5
# Developer: UY TRA
# Description:
# Read a list of timestamps and analyze the contents.
# Get the sum of all the values in timestamps.
# Then get the average and finally get the starting
# date and ending dates.
# Data will be in the Task 4 format and will be supplied as:
# W10_T5D1.txt and W10_T5D2.txt
# There are no check automation on this task so if it works it works.
#########################################################

import W10_T5Lib as Time


def menu():
    print('Choose operation:')
    print('1 - Show current date and time in ISO format')
    print('2 - Analytics')
    print('0 - Exit')
    choice = int(input('Your choice: '))
    if choice == 1:
        Time.showCurrentIsoFormat()
        menu()
    elif choice == 2:
        Time.readTimestampFromFile()
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
