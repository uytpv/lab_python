startVal = int(input("Give starting value: "))
stopVal = int(input("Give stopping value: "))
print()
print("Starting for loop:")
for i in range(startVal, stopVal+1):
    if i == stopVal:
        print(str(i))
    else:
        print(str(i), end = ' ')
print()
print("Thank you for using the program.")