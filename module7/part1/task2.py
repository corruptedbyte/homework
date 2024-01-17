def formatGreetingInner(name, age):
    if len(name) <= 0 or name.isspace():
        print("You must have a name!")
        return
    if age < 0:
        print("Age is too low!")
        return
    elif age > 130:
        print("Age is too high!")
        return
    if age > 1 or age < 1:
        return f"Hello, {name.capitalize()}. You are {age} years old"
    return f"Hello, {name.capitalize()}. You are 1 year old"

def formatGreetingOuter(name, age, yearold):
    if yearold: return f"Hello, {name.capitalize()}. You are 1 year old"
    return f"Hello, {name.capitalize()}. You are {age} years old"
    
name = "Artem"
age = 130
if len(name) <= 0 or name.isspace():
    print("You must have a name!")
    exit()
if age < 0:
    print("Age is too low!")
    exit()
elif age > 130:
    print("Age is too high!")
    exit()
if age > 1 or age < 1:
    print(formatGreetingOuter(name,age,False))
    exit()
print(formatGreetingOuter(name,age,True))