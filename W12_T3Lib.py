########################################################
# Task: W12_Lib
# Developer: Uy TRA
# Description:
# Library file for W12_XX tasks
#########################################################

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


def sum(data):
    data = convertToNumber(data)
    sum = 0
    for item in data:
        sum += item
    return sum


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


def display(type, data):
    if type == 'horizon':
        print('# --- Horizontally --- #')
        print(data)
        print('# --- Horizontally --- #')
    if type == 'vertical':
        print('# --- Vertically --- #')
        for item in data:
            print(item, end='\n')
        print('# --- Vertically --- #')
    if type == 'converted':
        print('# --- Converted --- #')
        print(data)
        print('# --- Converted --- #')
    if type == 'sum':
        print('# --- Sum of numbers --- #')
        print(str(sum(data)))
        print('# --- Sum of numbers --- #')
    if type == 'raw':
        print('# --- Raw data --- #')
        print(data)
        print('# --- Raw data --- #')
    if type == 'sort':
        print('# --- Sort data --- #')
        print(data)
        print('# --- Sort data --- #')
    return None
