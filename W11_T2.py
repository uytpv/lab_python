import sys
print('Welcome to the divider program.')
try:
    dividend = float(input('Insert dividend: '))
    divisor = float(input('Insert divisor: '))

    print('Operation: ' + str(dividend) + ' / ' +
          str(divisor) + ' = ' + str(dividend / divisor))
except ValueError:
    print('Couldn\'t convert the input into a number')
    sys.exit(1)
except ZeroDivisionError:
    print('Can\'t divide with 0')
    sys.exit(1)
finally:
    print('Thank you for using the program.')
