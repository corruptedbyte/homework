meters = int(input("Введіть довжину в метрах: "))
whatToShow = input("Вивести в милях, дюймах чи ярдах? (1,2 чи 3): ")

miles = meters*0.000621371192
inches = meters*39.3700787
yards = meters*1.0936133

match whatToShow:
    case "1":
        print(f"{meters} метрів у милях: {miles}")
    case "2":
        print(f"{meters} метрів у дюймах: {inches}")
    case "3":
        print(f"{meters} метрів у ярдах: {yards}")