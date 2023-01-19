startVal = int(input("Give starting value: "))
stopVal = int(input("Give stopping value: "))
print()
print("Starting while loop:")
i = startVal
while i <= stopVal:
    if i == stopVal:
        print(str(i))
        i+= 1
    else:
        print(str(i), end = ' ')
        i+= 1
print()
print("Thank you for using the program.")
