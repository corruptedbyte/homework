number = int(input("Введіть ваше число (2 цифри): "))

num1 = number%10
number = number//10

num2 = number%10
number = number//10

if (num1 == num2):
    print("Числа рівні")
else:
    print(num2, num1, sep=",", end=".")