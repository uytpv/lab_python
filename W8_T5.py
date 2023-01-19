def menu():
    print("Select one of the operations:")
    print("1) Print hello")
    print("2) Input string")
    print("3) Reverse string")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        print("Hello!", end="\n")
        print()
        menu()
    elif choice == 2:
        string = str(input("Give string: "))
        print("You inserted string: " + string, end="\n")
        print()
        menu()
    elif choice == 3:
        string = str(input("Give string: "))
        print("Your reversed string: " + string[::-1], end="\n")
        print()
        menu()
    elif choice == 0:
        print("Exiting.")
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.", end="\n")
        print()
        menu()

    return None


def main():
    menu()
    return None


main()
