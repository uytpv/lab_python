########################################################
# Task: W10_T3Lib
# Developer: UY TRA
# Description:
# Make a program which is able to sleep.
# Use separate files to achieve this.
# Recommended subprograms: sleepSecond, sleepForSeconds
#########################################################
import time


def sleepSecond():
    print('Going sleep for 1 second.')
    time.sleep(1)
    print('Slept 1 second. Continuing now...')
    print()
    return None


def sleepForSeconds():
    t = int(input('Give amount of seconds: '))
    print('Going sleep for \'' + str(t) + '\' second.')
    time.sleep(t)
    print('Slept for \'' + str(t) + '\' second. Continuing now...')
    print()
    return None
