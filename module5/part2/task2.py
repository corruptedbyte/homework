import random

funnyList = []
negativeNumberCount = 0
positiveNumberCount = 0

for i in range(0, 10):
    funnyList.append(random.randint(-10, 50))
for i in range(0, 10):
    if (funnyList[i] < 0):
        negativeNumberCount += 1
    else:
        positiveNumberCount += 1

print(funnyList)

if (funnyList.count(0) == 0):
    print("Zeroes: None")
else:
    print(f"Zeroes {funnyList.count(0)}")

print(f"Maximum: {max(funnyList)}")
print(f"Minimum: {min(funnyList)}")
print(f"Positive number count: {positiveNumberCount}")
print(f"Negative number count: {negativeNumberCount}")