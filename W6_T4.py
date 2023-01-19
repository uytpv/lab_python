def menu(count):
    print("Choose option below:", end="\n")
    print("1) Zero counter")
    print("2) Add count")
    print("3) Read count")
    print("0) Stop")
    choice = int(input("Give your choice: "))
    if choice == 1:
        count = zeroCounter(count)
        print()
        menu(count)
    elif choice == 2:
        count = addCount(count)
        print()
        menu(count)
    elif choice == 3:
        readCount(count)
        menu(count)
    elif choice == 0:
        print()
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        menu(count)

    return None


def zeroCounter(count):
    count = 0
    print("Zeroing count.")
    return count


def addCount(count):
    count = count +1
    print("Adding count.")
    return count


def readCount(count):
    print("Reading count.")
    print("Count is: " + str(count))
    print()
    return None


def main():
    count = 0
    print("This program acts like a typical counter.")
    menu(count)
    return None


main()
