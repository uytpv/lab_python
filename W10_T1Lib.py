########################################################
# Task: W10_T1Lib
# Developer: UY TRA
# Description: Make a menu-driven program which can
# perform sum and multiplication. Note! these should
# be in separate files e.g. W10_T1.py and W10_T1Lib.py.
# Recommended subprograms:
# askNumber,
# calculateSum,
# calculateMultiplication.
# Round the results always into two decimal precision.
#########################################################

def askNumber():
    return None


def calculateSum():
    print('Give two numbers and print sum of the numbers.')
    num1 = float(input('Give first number: '))
    num2 = float(input('Give second number: '))
    print(str(round(num1, 3)) + ' + ' + str(round(num2, 3)) +
          ' = ' + '{0:.2f}'.format(num1 + num2))
    print()
    return None


def calculateMultiplication():
    print('Give two numbers and print product of the numbers.')
    num1 = float(input('Give first number: '))
    num2 = float(input('Give second number: '))
    print(str(round(num1, 3)) + ' * ' + str(round(num2, 3)) +
          ' = ' + '{0:.2f}'.format(num1 * num2))
    print()
    return None
