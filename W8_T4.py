number = int(input("Give a number: "))
print("You gave a number value: " + str(number))
if (number > 0 and number < 10):
    if (number % 2 == 0):
        print("Number value is between 0 and 10. Number is even.")
    else:
        print("Number value is between 0 and 10. Number is odd.")
elif number > 10:
    print("Number is greater than or equal to 10")
    print("Number multiplied by 10 is " + str(number * 10))
elif number == 0:
    print("Value was 0.")
else:
    print("It is a negative number.")
print("Thank you for using the program.")
