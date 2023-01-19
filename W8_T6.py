def menu():
    print("Select one of the operations:")
    print("1) Add numbers")
    print("2) Multiply numbers")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        addition()
        menu()
    elif choice == 2:
        multiplication()
        menu()
    elif choice == 0:
        print("Exiting.")
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        print()
        menu()

    return None


def addition():
    number_1 = float(input("Give a number: "))
    number_2 = float(input("Give a number: "))
    print("Sum is: " + str(round(number_1 + number_2, 2)))
    print()
    return None


def multiplication():
    number_1=float(input("Give a number: "))
    number_2=float(input("Give a number: "))
    print("Product is: " + str(round(number_1 * number_2, 2)))
    print()
    return None


def main():
    menu()
    return None


main()
