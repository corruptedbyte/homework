def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)

def largestDivisor(*numbers):
    print(list(factorial(num) for num in numbers))