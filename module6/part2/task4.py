def removeFromList(numList, toRemove):
    count = 1
    for i in numList:
        if i == toRemove:
            numList.remove(i)
            count += 1
    return count

coolList = [5,5,5,3,2]
result = removeFromList(coolList, 5)
print(result)