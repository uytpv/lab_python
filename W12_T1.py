########################################################
# Task: W12_T1
# Developer: Uy TRA
# Description:
# Create a program which asks user to insert filename and then display the results
# in two different ways.
# While reading the file rows, strip the newline characters from the rows and also
# remove empty rows, then return the rows.
# Finally display the rows in two different ways:
# - Horizontally, by printing the list of rows itself.
# - Vertically, by printing each row on separate row.
#   + Recommendation: create a separate subprogram for this part
# Example file data10.txt
#########################################################
import W12_T3Lib as Lib


def main():
    print('Welcome to the program.')
    fileName = input('Insert filename: ')
    data = Lib.readFile(fileName)
    Lib.display('horizon', data)
    Lib.display('vertical', data)
    print('Thank you for using the program.')
    return None


def menu():
    return None


main()
