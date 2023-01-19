print("Give two integers.")
firstNumber = int(input("Give first number: "))
secondNumber = int(input("Give second number: "))

print("Let's find out which number is greater.")
if firstNumber > secondNumber :
    print ("First number is greater.")
elif secondNumber > firstNumber :
    print ("Second number is greater.")
else :
    print("Numbers are the same.")
print("Let's find out if the numbers are even.")
if firstNumber % 2 == 0 :
    print ("First number is even.")
else :
    print ("First number is odd.")
if secondNumber % 2 == 0 :
    print ("Second number is even.")
else :
    print ("Second number is odd.")

print("Thank you for using the program.")
