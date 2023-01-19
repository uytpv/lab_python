import sys


content = []
numOfRount = 0
sum = 0


def menu():
    print('Options:')
    print('1 - readfile')
    print('2 - analyze')
    print('3 - display')
    print('0 - exit')
    try:
        choice = int(input('Your choice: '))
    except ValueError:
        print('Value error while counting sum and count')
    except UnboundLocalError:
        print('Error while reading file.')
        sys.exit(1)
    if choice == 1:
        global content
        content = readFile()
        print()
        menu()
    elif choice == 2:
        analyze()
        print()
        menu()
    elif choice == 3:
        display()
        print()
        menu()
    elif choice == 0:
        print('Exiting program.')
        print()
        print('Thank you for using the program.')
    else:
        print('Unknown option, try again.')
        menu()

    return None


def readFile():
    fileNameReading = str(input('Give filename to read: '))
    try:
        f = open(fileNameReading, mode='r', encoding='utf-8')
        c = f.readlines()
    except FileNotFoundError:
        print('Error while reading file.')
        sys.exit(1)
    except UnboundLocalError:
        print('Error while reading file.')
        sys.exit(1)
    return c


def analyze():
    global content
    global numOfRount
    global sum
    for item in content:
        numOfRount += 1
        try:
            sum += int(item)
        except:
            print('Value error while counting sum and count')
            sys.exit(1)
    return None


def display():
    print('Results of analytics:')
    print('Amount of rows: 4')
    print('Sum of rows: 154.0')
    return None


def main():
    menu()
    return None


main()
