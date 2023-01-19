startingPoint = int(input("Give starting point: "))
stoppingPoint = int(input("Give stopping point: "))
inspectionPoint = int(input("Give inspection point: "))
if inspectionPoint > stoppingPoint or inspectionPoint < startingPoint:
    print()
    print("Inspection has to be within the range.")
    print("Thank you for using the program.")
else:
    print()
    print("First loop:")
    for i in range(startingPoint, stoppingPoint):
        if i == inspectionPoint:
            print(str(i))
            break
        else:
            print(str(i), end = " ")
    print()
    print("Second loop:")

    for i in range(startingPoint, stoppingPoint + 1):
        if i == inspectionPoint:
            continue
        else:
            if i == stoppingPoint:
                print(str(i))
            else:
                print(str(i), end = " ")
    print()
    print("Thank you for using the program.")

