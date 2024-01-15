# import math
import os

# Classwork, minidictionary save


# try:
#     intake = int(input("Enter a number:"))
#     if intake < 0:
#         print("Ain't no way you used a negative number.")
#     print(math.sqrt(intake))
# except ValueError:
#     print("Aye you can't use letters mate!")
# except ZeroDivisionError:
#     print("Why the hell do you wanna square a minus?")
# else:
#     print("Awesome.")

# def getASquareRoot(num):
#     return math.sqrt(num)

# def getASquareRootChecked(num):
#     if num < 0:
#         return 0
#     return math.sqrt(num)

# print(getASquareRootChecked(10))

def addToDict(dictionary, queryKeyName, queryContent):
    dictionary[queryKeyName] = queryContent
    return dictionary

def edit(dictionary):
    query1 = input("Enter key name > ")
    query2 = input("Enter key content > ")
    return addToDict(dictionary, query1, query2)

def show(dictionary):
    try:
        query = input("Enter key name to display > ")
        print(dictionary[query])
    except KeyError:
        print("Unknown key")

dictionary = {}

print("MINI Dictionary v1.0")

while True:
    query = input("> ")
    match query:
        case "edit":
            dictionary = edit(dictionary)

        case "show":
            print(dictionary)

        case "showKey":
            show(dictionary)

        case "clear":
            os.system("cls")

        case "exit":
            exit()