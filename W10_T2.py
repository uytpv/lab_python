########################################################
# Task: W10_T2
# Developer: UY TRA
# Description: Continue the previous task and add average calculations into it
#########################################################

import W10_T2Lib as Cal


def menu():
    print("Choose operation:")
    print("1) Sum")
    print("2) Multiplication")
    print("3) Average")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        Cal.calculateSum()
        menu()
    elif choice == 2:
        Cal.calculateMultiplication()
        menu()
    elif choice == 3:
        Cal.average()
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
