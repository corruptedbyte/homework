number = int(input("Введіть ваше число (3 цифри): "))
mode = input("Вивести суму чи добуток (1 чи 2?): ")

num1 = number%10
number = number//10

num2 = number%10
number = number//10

num3 = number%10
number = number//10

match mode:
    case "1":
        print(f"Ваша сума чисел: {num1+num2+num3}")
    case "2":
        print(f"Ваш добуток чисел: {num1*num2*num3}")
    case _:
        print("Неможливо вивести результати (неправильний формат)")