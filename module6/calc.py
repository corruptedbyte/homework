def subadd(num1, num2, boolOperation=True):
    if boolOperation:
        return num1+num2
    return num1-num2

def muldiv(num1, num2, boolOperation=True):
    if boolOperation:
        return num1*num2
    return num1/num2

print("0 - Exit\n1 - Add\n2 - Substract\n3 - Multiply\n4 - Divide")

while True:
    match int(input("~> ")):
        case 0:
            print("Goodbye.")
            exit()
        case 1:
            nums = input("(Enter two numbers and split them using a space) ~> ").split()
            print(subadd(int(nums[0]),int(nums[1])))
        case 2:
            nums = input("(Enter two numbers and split them using a space) ~> ").split()
            print(subadd(int(nums[0]),int(nums[1]), False))
        case 3:
            nums = input("(Enter two numbers and split them using a space) ~> ").split()
            print(muldiv(int(nums[0]),int(nums[1])))
        case 4:
            nums = input("(Enter two numbers and split them using a space) ~> ").split()
            print(muldiv(int(nums[0]),int(nums[1]), True))
