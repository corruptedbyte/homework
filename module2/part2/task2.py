# Getting the values (once again)

e0 = int(input("Введіть число в 4 символа: "))

if e0 < 4:
    exit()

e = e0

e1 = e%10
e = e // 10

e2 = e%10
e = e // 10

e3 = e%10
e = e // 10

e4 = e%10
e = e // 10

answer = e1*e2*e3*e4

print(f"Відповідь: {answer}")