x = int((input("Enter x:")))
# using abs() gives correct
# last digit for negative nos
lastDigit = abs(x) % 10
print ("Last Digit is", lastDigit)