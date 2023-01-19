########################################################
# Task: W10_T2Lib
# Developer: UY TRA
# Description: Continue the previous task and add average calculations into it
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


def average():
    print('Counting average, give numbers first.')
    numbers = []
    index = 1
    num = float(input('Give 1st number. 0 to stop: '))
    while num > 0:
        numbers.append(num)
        index += 1
        if (index == 2):
            num = float(input('Give 2nd number. 0 to stop: '))
        elif (index == 3):
            num = float(input('Give 3rd number. 0 to stop: '))
        else:
            num = float(input('Give ' + str(index) + 'th number. 0 to stop: '))

    sum = 0
    for number in numbers:
        sum += number

    print('Amount of inserted numbers: ' + str(len(numbers)))
    print('Average of the inserted numbers: ' +
          '{0:.2f}'.format(sum/len(numbers)))
    print()
    return None
