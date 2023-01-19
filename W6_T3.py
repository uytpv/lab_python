

def menu(string, hyphenate):
    print("Choose option below:", end="\n")
    print("1) Give a string")
    print("2) Give a hyphenate")
    print("3) Output results")
    print("0) Stop")
    choice = int(input("Give your choice: "))
    if choice == 1:
        string = askString()
        print()
        menu(string, hyphenate)
    elif choice == 2:
        hyphenate = askHyphenate()
        print()
        menu(string, hyphenate)
    elif choice == 3:
        outputResults(string, hyphenate)
        menu(string, hyphenate)
    elif choice == 0:
        print()
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        menu(string, hyphenate)

    return None


def askString():
    return str(input("Give a string: "))


def askHyphenate():
    return str(input("Give a hyphenate: "))


def outputResults(string, hyphenate):
    outputString = ""
    key = 1
    for c in string:
        if (key < len(string)):
            outputString = outputString + c + hyphenate
        else:
            outputString = outputString + c
        key = key + 1
    print(outputString)
    return None


def main():
    string = ""
    hyphenate = ""
    print("This program can print strings with different hyphenates.")
    menu(string, hyphenate)
    return None


main()
