########################################################
# Task: W10_T5
# Developer: UY TRA
# Description:
# Read a list of timestamps and analyze the contents.
# Get the sum of all the values in timestamps.
# Then get the average and finally get the starting
# date and ending dates.
# Data will be in the Task 4 format and will be supplied as:
# W10_T5D1.txt and W10_T5D2.txt
# There are no check automation on this task so if it works it works.
#########################################################
import datetime as dt
import csv


def showCurrentIsoFormat():
    print('Time and date in ISO format: ' + str(dt.datetime.now().isoformat()))
    print()
    return None


def readTimestampFromFile():
    fileName = str(input('File name: '))
    f = open(fileName, mode='r', encoding='utf-8')
    dataList = f.readlines()
    analyze(dataList)
    print()
    return None


def analyze(dataList):
    content = []
    count = 0
    sum = 0
    firstDay = None
    endDay = None
    for line in dataList:
        if (count > 0):
            if ("\n" in line):
                dataList[count] = line.rstrip()
            obj = TimeStamp()
            obj.Datetime = dataList[count].split(';')[0]
            obj.Value = dataList[count].split(';')[1]
            content.append(obj)
        count += 1
    for obj in content:
        sum += int(obj.Value)
        day = dt.datetime.strptime(obj.Datetime, '%Y-%m-%dT%H:%M')
        if (firstDay == None):
            firstDay = day
        elif (firstDay > day):
            firstDay = day

        if (endDay == None):
            endDay = day
        elif (endDay < day):
            endDay = day

    print('Sum = ' + str(sum) + ' - Average = ' + str('{0:.2f}'.format(sum/count)))
    print('Starting Day: ' + firstDay.strftime('%Y-%m-%d %H:%M'))
    print('Ending Day: ' + endDay.strftime('%Y-%m-%d %H:%M'))

    return None


class TimeStamp ():
    Datetime = None
    Value = None
