# Take a number and print square of a number if it is less than 10

n = int(input("Enter a number less than to print its square"))

if n < 10:
    n = n * n
    print("The square of a  number is ", n)
else:
    print("Entered number is greater than 10")
