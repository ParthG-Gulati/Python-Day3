# Swap 2 numbers without using third variable

a = int(input("Enter first number"))
b = int(input("Enter second number "))

a = a + b
b = a - b
a = a - b

print("Value of first number after swap is:", a)
print("Value of second number after swap is:", b)
