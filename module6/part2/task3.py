def isPrime(numList):
    count = 0
    for i in range(0, len(numList)):
        if numList[i] / 1 == 1 and numList[i] / numList[i] == 1:
            count += 1
    return count

print(isPrime([1,1,1,1]))