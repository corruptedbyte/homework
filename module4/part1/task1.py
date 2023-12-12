rangeStart = int(input("Enter starting number: "))
rangeEnd = int(input("Enter ending number: "))

if rangeStart > rangeEnd:
    print("Starting number is too big!")
    exit()

for i in range(rangeStart, rangeEnd):
    if i % 7 == 0:
        print(i)
print(f"Numbers multiple by 7 that range from {rangeStart} to {rangeEnd}")