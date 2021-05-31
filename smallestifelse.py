# Smallest of 3 numbers using logical operator

a = int(input("Enter first number"))
b = int(input("Enter second number "))
c = int(input("Enter third number "))

if a < b and a < c:
    print(a, "is smallest")
elif b < c:
    print(b, "is smallest")
else:
    print(c, "is smallest")
