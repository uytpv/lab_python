class TASK:
    Name = None
    Status = ' '


Tasks = []


def menu():
    print("Options:")
    print("1) Insert task")
    print("2) Mark done")
    print("3) Display todos")
    print("4) Export to file")
    print("0) Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        insertTask()
        menu()
    elif choice == 2:
        markDone()
        menu()
    elif choice == 3:
        displayTask()
        menu()
    elif choice == 4:
        export()
        menu()
    elif choice == 0:
        print("Exiting.")
        print("Thank you for using the program.")
    else:
        print("Unknown option, try again.")
        print()
        menu()

    return None


def insertTask():
    task = TASK()
    task.Name = str(input('Insert task name: '))
    Tasks.append(task)
    print()
    return None


def markDone():
    print('Here is list of todos:')
    index = 0
    for task in Tasks:
        print(' - ' + str(index + 1) + '. ' + task.Name)
        index += 1
    choose = int(input('Give task number to mark it done: '))
    Tasks[choose - 1].Status = 'x'
    # if (Tasks[choose - 1].Status == 'x'):
    #     Tasks[choose - 1].Status = ' '
    # else:
    #     Tasks[choose - 1].Status = 'x'
    print()
    return None


def displayTask():
    print('TODOs:')
    for task in Tasks:
        print(' - [' + task.Status + '] ' + task.Name)
    print()
    return None


def export():
    f = open('data.txt', mode='w', encoding='utf-8')
    for task in Tasks:
        if (task.Status == 'x'):
            s = 'done'
        else:
            s = 'undone'
        f.write(task.Name + ';' + s + '\n')
    f.close()
    return None


def main():
    print('Welcome to TODO app!')
    menu()
    return None


main()
