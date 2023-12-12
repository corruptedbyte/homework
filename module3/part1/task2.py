number = int(input("Введіть ваше число (3 цифри): "))
mode = input("Вивести мінимум, максимум чи середьє арифматичне? (1,2 чи 3): ")

num1 = number%10
number = number//10

num2 = number%10
number = number//10

num3 = number%10
number = number//10

match mode:
    case "1":
        print(f"Мінімум чисел: {min(num1, num2, num3)}")
    case "2":
        print(f"Максимум чисел: {max(num1, num2, num3)}")
    case "3":
        print(f"Середньє арифматичне чисел: {(num1+num2+num3)/3}")