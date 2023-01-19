firstNumber = int(input("Give first number: "))
secondNumber = int(input("Give second number: "))

print("Our values are:")
print("First number - " + str(float(firstNumber)))
print("Second number - " + str(float(secondNumber)))
if firstNumber > secondNumber:
    print("The first number is greater than the second number.")
elif firstNumber == secondNumber:
    print("Numbers are equal")
else:
    print("The first number is lesser than the second number.")
print("Thank you for using the program.")
2