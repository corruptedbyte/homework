rangeStart = int(input("Enter starting number: "))
rangeEnd = int(input("Enter ending number: "))

for i in range(rangeStart, rangeEnd):
    if (i % 3 == 0 and i % 5 == 0):
        print("Fizz Buzz")
    elif (i % 3 == 0):
        print("Fizz")
    else:
        print("Buzz")