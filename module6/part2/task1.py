def productOfList(numList):
    product = 1
    for i in numList:
        product *= i
    return product

print(productOfList([1,2,3]))