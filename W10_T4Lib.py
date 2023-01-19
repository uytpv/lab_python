########################################################
# Task: W10_T4Lib
# Developer: UY TRA
# Description:
# Create program which is able to read timestamp from a file.
# Timestamp in this context means that there are two fields,
# Datetime field and Value field.
# Data: W10_T4D1.txt
#########################################################
import datetime as dt
import csv


def readFile():
    f = open('W10_T4D1.txt', mode='r', encoding='utf-8')
    listData = list(csv.reader(f, delimiter=';'))
    return listData[1]


def showCurrentIsoFormat():
    print('Time and date in ISO format: ' + str(dt.datetime.now().isoformat()))
    print()
    return None


def readTimestampFromFile():
    print()
    return readFile()


def printTimestamp(timeStamp):
    date = dt.datetime.strptime(timeStamp[0], '%Y-%m-%dT%H:%M')
    print('Displaying timestamp.')
    print('Timestamp details - date: ' + date.strftime('%Y-%m-%d') + ', time: ' +
          date.strftime('%H:%M') + ', value: ' + timeStamp[1])
    print()        
    return None
