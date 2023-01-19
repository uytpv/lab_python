########################################################
# Task: W12_T2
# Developer: Uy TRA
# Description:
# Create program which does the W12_T1 things, but change the program a bit.
# Instead of displaying data vertically and horizontally, do the following steps:
# - Dislay the list of rows horizontally
# - Convert the rows into numbers
# - Display the list of numbers horizontally
# - Calculate the sum of the numbers
#   + Recommendation: create a subprogram to do this task
# - Display the sum of numbers
# Data is the same and the expected format can be seen below.

#########################################################
import W12_T3Lib as Lib


def main():
    print('Welcome to the program.')
    fileName = input('Insert filename: ')
    data = Lib.readFile(fileName)  # raw data
    Lib.display('horizon', data)  # string data
    Lib.display('converted', Lib.convertToNumber(data))  # number data
    Lib.display('sum', Lib.convertToNumber(data))  # sum of numbers
    print('Thank you for using the program.')
    return None


def menu():
    return None


main()
