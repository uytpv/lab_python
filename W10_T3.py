########################################################
# Task: W10_T3
# Developer: UY TRA
# Description:
# Make a program which is able to sleep.
# Use separate files to achieve this.
# Recommended subprograms: sleepSecond, sleepForSeconds
#########################################################

import W10_T3Lib as Sleep


def menu():
    print("Choose operation:")
    print("1) Sleep 1 second")
    print("2) Sleep x amount of seconds")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        Sleep.sleepSecond()
        menu()
    elif choice == 2:
        Sleep.sleepForSeconds()
        menu()
    elif choice == 0:
        print("Exiting.")
        print()
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        print()
        menu()

    return None


print('Welcome to the program.')
menu()
