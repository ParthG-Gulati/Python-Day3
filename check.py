# Check wether entered number is positive, negative or zero

n = int(input("Enter a number"))
if n >= 0:
    if n == 0:
        print("n is zero")
    else:
        print("n is positive")
else:
    print("Entered number is negative")
