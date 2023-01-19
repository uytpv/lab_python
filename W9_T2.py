class TASK:
    Name = None
    Status = ' '


def showTasks():
    print('Task: ' + task1.Name+', status: "'+task1.Status+'"')
    print('Task: ' + task2.Name+', status: "'+task2.Status+'"')
    print()
    return None


task1 = TASK()
task2 = TASK()

task1.Name = str(input('Give first task name: '))
task2.Name = str(input('Give second task name: '))
showTasks()
print('Change task one (1) or task two (2)')
choice = int(input('Your choice(1 or 2): '))
if (choice == 1):
    task1.Status = 'x'
if (choice == 2):
    task2.Status = 'x'
showTasks()
print('Thank you for using the program.')