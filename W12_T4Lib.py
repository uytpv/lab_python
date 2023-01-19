import time as time


def readFile(fileName):
    fileData = open(fileName,  mode='r', encoding="UTF-8")
    dataArr = []
    for line in fileData:
        if line != "\n":  # Remove blank line
            Content = line.rstrip('\n')
            dataArr.append(Content)
    fileData.close()
    return dataArr


def convertToNumber(data):
    dataNumber = []
    for item in data:
        dataNumber.append(float(item))
    return dataNumber


def bubblesort(inArray):
    data = inArray.copy()
    n = len(data)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                swapped = True
                data[j], data[j + 1] = data[j + 1], data[j]
        if not swapped:
            return data
    return data


def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
