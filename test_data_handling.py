# Data handling

def askFilename():
    Feed = input("Give a filename: ")
    return Feed

def readFile(Filename):
    Filehandle = open(Filename, 'r', encoding="UTF-8")
    Rows = []
    # remove newline charaters and empty rows
    while True:
        Row = Filehandle.readline()
        if len(Row) == 0: # Row has no newline character
            break
        elif len(Row) == 1: # Row has only newline character
            pass
        else:
            Content = Row.rstrip('\n')
            Rows.append(Content)
    Filehandle.close()
    return Rows

# Convert strings into numbers

def summary(Rows):
    Results = 0
    for Row in Rows:
        Results = Results + Row
    return Results

def bubblesort(Rows):
    return None

def main():
    Rows = []
    Results = []
    Filename = askFilename()
    Rows = readFile(Filename)
    print(Rows)

    # Sort quickly
    Rows.sort()
    print(Rows)

    #Converted = Rows # its a pointer to a list
    Converted = [float(Row) for Row in Rows]
    print(Converted)

    # just to demo sorting on floats
    Converted.sort()
    print(Converted)

    # summary
    Results = summary(Converted)
    print(Results)
    return None

main()
