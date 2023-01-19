def askFilename(string):
    filename = str(input(string))
    return filename


def checkRow(fileName, isLetter):
    f = open(fileName, mode='r', encoding='utf-8')
    len = 0
    isalpha = 0
    for line in f:
        if line != "\n":
            for c in line:
                if c != "\n":
                    len += 1
                    if c.isalpha():
                        isalpha += 1

    if isLetter:
        return isalpha
    else:
        return len - isalpha


def storeResults(letters, nonletters, fileNameWriting):
    f = open(fileNameWriting, mode='w', encoding='utf-8')
    f.write("The results of analytics.\n")
    f.write("File contained " + str(letters) + " letters\n")
    f.write("and " + str(nonletters) + " non-letters\n")
    f.close()
    return None


def main():
    fileNameReading = askFilename("Give filename to read: ")
    fileNameWriting = askFilename("Give filename to write: ")

    storeResults(checkRow(fileNameReading, True),
                 checkRow(fileNameReading, False), fileNameWriting)


main()
