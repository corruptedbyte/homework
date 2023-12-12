#daysAWeek = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"]

# we all hate mondays, don't you think?

day = int(input("Введіть 1 день тижня (1-7): "))

match day:
    case 1:
        print("Понеділок")
    case 2:
        print("Вівторок")
    case 3:
        print("Середа")
    case 4:
        print("Четвер")
    case 5:
        print("П'ятниця")
    case 6:
        print("Субота")
    case 7:
        print("Неділя")