# Take a number a check if it is negative positive or zero using if else statement

n = int(input("Enter a number"))

if n >= 0:
    if n > 0:
        print(n, "is positive ")
    else:
        print(n, " is zero")
else:
    print(n, " is negative")
