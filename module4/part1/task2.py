rangeStart = int(input("Enter starting number: "))
rangeEnd = int(input("Enter ending number: "))

if rangeStart > rangeEnd:
    print("Starting number is too big!")
    exit()

multipleBy5 = 0

for i in reversed(range(rangeStart, rangeEnd)):
    print(i)
    if i % 7 == 0:
        print(f"{i} is multiple by 7")
    if i % 5 == 0:
        multipleBy5 += 1

print(f"{multipleBy5} numbers are multiple by 5")