# Program to Check if a Number is Positive, Negative or 0

num = float(input("Enter a number: "))  # Taking user input and converting it to float

if num > 0:
    print("Positive number")  # If the number is greater than 0, print "Positive number"
elif num == 0:
    print("Zero")  # If the number is exactly 0, print "Zero"
else:
    print("Negative number")  # If the number is less than 0, print "Negative number"
