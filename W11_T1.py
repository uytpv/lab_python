import sys

def main():
    max = 0
    print('Welcome to the highest value program.')
    print('Currently the highest value is: ' + str(max))
    try:
        prompt = float(input('Insert new value (0 to exit): '))

        while (prompt != 0):
            print('Updating the highest value.')
            if (prompt > max):
                max = prompt
            print()
            print('Currently the highest value is: ' + str(max))
            prompt = float(input('Insert new value (0 to exit): '))
        else:
            print('Highest value was ' + str(max))
            print('Thank you for using the program.')
    except ValueError:
        print('Error happened in the program, program exiting properly.')
        sys.exit(1)

    return None


main()
