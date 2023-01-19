fileNameReading = ""
fileNameWriting = ""
content = []


def askFilename(string):
    filename = str(input(string))
    return filename


def menu():
    print("Select one of the operations:")
    print("1) Read file")
    print("2) Analyze")
    print("3) Write file")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        global content
        content = readFile(fileNameReading)
        print("Read operation completed.")
        print()
        menu()
    elif choice == 2:
        analyze()
        print("Analyze operation completed.")
        print()
        menu()
    elif choice == 3:
        writeFile(fileNameWriting, content)
        print("Write operation completed.")
        print()
        menu()
    elif choice == 0:
        print("Exiting.")
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        menu()

    return None


def readFile(fileName):
    f = open(fileName, mode='r', encoding='utf-8')
    c = f.readlines()
    return c


def writeFile(fileNameWriting, content):
    f = open(fileNameWriting, mode='w', encoding='utf-8')
    for item in content:
        f.write(f"{item}")
    f.close()
    return None


def analyze():
    global content
    count = 0
    for item in content:
        if (item[-1] == "e" or item[-1] == "E"):
            content[count] = item[:-1]
        if ("\n" in item):
            content[count] = item.rstrip()
        count += 1
    return None


def main():
    global fileNameReading
    global fileNameWriting
    fileNameReading = askFilename("Give filename to read: ")
    fileNameWriting = askFilename("Give filename to write: ")
    menu()
    return None


main()
