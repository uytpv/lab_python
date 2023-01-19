def outputInstructions():
    print("This program looks for the smaller input.", end="\n")
    print("In the end, the program tells count of numbers inputted and the smallest number.", end="\n")
    print()
    return None


def askInteger():
    count = 0
    number = int(input("Give a positive integer: "))

    if number != 0:
        count += 1
        smallestNumber = number
        while number != 0:
            newNumber = int(input("Give a new positive integer (0 stops): "))

            if newNumber != 0:
                count += 1
                if smallestNumber > newNumber:
                    smallestNumber = newNumber
            else:
                number = 0
                outputResults(count, smallestNumber)
    else:
        outputResults(count, smallestNumber)

    return None


def outputResults(count, smallestNumber):
    if count > 1:
        print()
        print("You gave " + str(count) + " numbers.")
        print("The smallest number was " + str(smallestNumber) + ".", end="\n")
        print("Thank you for using the program.")
        return None
    else:
        print()
        print("You gave only one number, which was " + str(smallestNumber) + ".")
        print("Thank you for using the program.")


def main():
    outputInstructions()
    askInteger()
    return None


main()
