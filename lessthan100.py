# Check wether a number is less than 100 or not
# If it is less than 100 check it is even or odd

n = int(input("Enter a number"))

if n < 100:
    if n % 2 == 0:
        print("Entered number is Even")
    else:
        print("Entered number is Odd")
else:
    print("Entered number is greater than 100")
