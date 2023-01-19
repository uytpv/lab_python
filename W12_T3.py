########################################################
# Task: W12_T3
# Developer: Uy TRA
# Description:
# Create a program which is able to read file and handle the file content. First ask
# the user to insert filename. Read the requested file and during the read
# operation, skip empty rows and remove the newline characters from each row.
# Insert rows into a list variable and then display the raw data in the list.
# Then create a subprogram called bubblesort and do the following operations:
# - Sort the raw data in ascending order with the bubblesort subprogram and display the result
# - Convert the raw data rows into numbers (see example run) and display the result
# - Sort the converted data in ascending order with the bubblesort subprogram and display the result


#########################################################
import W12_T3Lib as Lib


def main():
    print('Welcome to the program.')
    fileName = input('Insert filename: ')
    data = Lib.readFile(fileName)  # raw data
    Lib.display('raw', data)  # string data

    dataSorted = Lib.bubblesort(data)
    Lib.display('sort', dataSorted)  # number data

    print('# --- Converting --- #')
    dataNumber = Lib.convertToNumber(data)
    print(dataNumber)
    print('# --- Converted --- #')

    Lib.display('sort', Lib.bubblesort(dataNumber))  # number data
    print('Thank you for using the program.')
    return None


def menu():
    return None


main()
