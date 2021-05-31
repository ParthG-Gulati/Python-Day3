# Take two numbers and display greatest numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if a >= b:
    if a > b:
        print(a,  "is greater")
    else:
        print("Both numbers are equal")
else:
    print(b, "is greater")
