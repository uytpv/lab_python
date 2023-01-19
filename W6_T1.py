def outputInstructions():
    print("This program asks filename and extension. Then outputs filename with extension.", end="\n")
    print("Give first filename and then the file extension without a dot.", end="\n")
    print()
    return None


def askQuestion():
    print("This subprogram asks user input.")
    fileName = str(input("Give filename: "))
    print("This subprogram asks user input.")
    extension = str(input("Give file extension: "))
    outputResults(fileName, extension)
    return None


def outputResults(fileName, extension):
    print("This subprogram prints filename with the file extension.")
    print("Filename: " + fileName + "." + extension, end="\n")
    print()
    print("Thank you for using the program.")
    return None


def main():
    outputInstructions()
    askQuestion()
    return None


fileName = ""
extension = ""
main()
