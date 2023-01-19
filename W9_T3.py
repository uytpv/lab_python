class TASK:
    Name = None
    Status = ' '


task = TASK()


def menu():
    print("Options:")
    print("1) Set task name")
    print("2) Change task status")
    print("3) Display task")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        setTaskName()
        menu()
    elif choice == 2:
        changeTaskStatus()
        menu()
    elif choice == 3:
        displayTask()
        menu()
    elif choice == 0:
        print("Exiting.")
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        print()
        menu()

    return None


def setTaskName():
    task.Name = str(input('Set task name: '))
    print()
    return None


def changeTaskStatus():
    if(task.Status == 'x'):
        task.Status = ' '
    else:
        task.Status = 'x'
    print()
    return None


def displayTask():
    print('Task: ' + task.Name + ', status: "' + task.Status + '"')
    print()
    return None


def main():
    menu()
    return None


main()
