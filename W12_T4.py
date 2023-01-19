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
import W12_T4Lib as Lib
import time as time


def main():
    print('Welcome to the program.')
    fileName = input('Insert filename: ')

    print('# --- Raw data --- #')
    sTime1 = time.time()
    data = Lib.readFile(fileName)  # raw data
    # time.sleep(2)
    eTime1 = time.time()
    diff1 = (eTime1 - sTime1)
    print('Reading: %f milliseconds' % diff1)
    print('# --- Raw data --- #')

    print('# --- Converting --- #')
    sTime2 = time.time()
    Lib.convertToNumber(data)  # Convert data
    eTime2 = time.time()
    diff2 = (eTime2 - sTime2)
    print('Conversion: %f milliseconds' % diff2)
    print('# --- Converted --- #')

    print('# --- Bubblesort --- #')
    sTime3 = time.time()
    Lib.bubblesort(data)  # Convert data
    eTime3 = time.time()
    diff3 = (eTime3 - sTime3)
    print('Bubblesort: %f milliseconds' % diff3)
    print('# --- Bubblesort --- #')

    print('# --- Quicksort --- #')
    sTime4 = time.time()
    Lib.quickSort(data, 0, len(data)-1)  # Convert data
    eTime4 = time.time()
    diff4 = (eTime4 - sTime4)
    print('Quicksort: %f milliseconds' % diff4)
    print('# --- Quicksort --- #')

    print('Thank you for using the program.')
    return None


main()
