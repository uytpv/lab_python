########################################################
# Task: W10_T1
# Developer: UY TRA
# Description: Make a menu-driven program which can
# perform sum and multiplication. Note! these should
# be in separate files e.g. W10_T1.py and W10_T1Lib.py.
# Recommended subprograms:
# askNumber,
# calculateSum,
# calculateMultiplication.
# Round the results always into two decimal precision.
#########################################################

import W10_T1Lib as Cal


def menu():
    print("Choose operation:")
    print("1) Sum")
    print("2) Multiplication")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        Cal.calculateSum()
        menu()
    elif choice == 2:
        Cal.calculateMultiplication()
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
