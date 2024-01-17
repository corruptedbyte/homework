print("Introduce yourself :)")

name = input("Enter your name: ")
if len(name) <= 0 or name.isspace():
    print("You must have a name!")
    exit()

try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age is too low!")
    elif age > 130:
        print("Age is too high!")
except ValueError:
    print("Your age must only contain numbers!")