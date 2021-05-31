# Factorial of a number

n = int(input("Enter a number to find factorial"))
factorial = 1

while n > 0:
    factorial = factorial * n
    n = n-1
print("Factoial of the number is :", factorial)
