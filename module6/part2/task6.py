def squareList(square, numList):
    result = []
    for i in numList:
        squared = i ** square
        result.append(squared)
    return result

print(squareList(2, [1,2,3,4]))