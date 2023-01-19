intNum = 0
print('Welcome to the binary value converter.')


def menu():
    global intNum
    print("Options:")
    print("1 - Pick integer in range 0 - 255")
    print("2 - Present number in binary")
    print("3 - Present number in hexadecimal")
    print("4 - Present number in ASCII")
    print("5 - Present number Unicode name alias")
    print("0 - Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        intNum = int(input('Give an integer between 0 and 255: '))
        print(intNum)
        menu()
    elif choice == 2:
        print('Value: ' + str(intNum) + ' in binary format is - \'' +
              bin(intNum) + '\'')
        menu()
    elif choice == 3:
        print('Value: ' + str(intNum) + ' in hex format is - \'' +
              hex(intNum) + '\'')
        menu()
    elif choice == 4:
        print('Value: ' + str(intNum) + ' in ASCII format is - \'' +
              chr(intNum) + '\'')
        menu()
    elif choice == 5:
        toUnicode(intNum)
        menu()
    elif choice == 0:
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        menu()

    return None


def toUnicode(num):
    print('Value: ' + str(num) + ' in UTF-8 format is - \'\'')
    unicodeNum = str(chr(num))
    print((unicodeNum))
    arr = readFile('NameAliases.txt')
    aliasName = []
    for item in arr:
        if (item[0]) == unicodeNum:
            aliasName.append(item)

    print(aliasName, end='\n')
    return None


def readFile(fileName):
    fileData = open(fileName,  mode='r', encoding="UTF-8")
    dataArr = []
    for line in fileData:
        if (line[0] != '#'):
            if line != "\n":  # Remove blank line
                Content = line.rstrip('\n')
                dataArr.append(Content.split(';'))
    fileData.close()
    return dataArr


def main():
    menu()


main()
