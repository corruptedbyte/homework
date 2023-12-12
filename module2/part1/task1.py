# Getting 3 values from the user
x = int(input("Число 1: "))
y = int(input("Число 2: "))
z = int(input("Число 3: "))

# Make a sum by adding those values together
sum = x+y+z
# Same thing but instead of adding the values we multiply by them (zeroes are allowed because it's not division)
product = x*y*z

# Print the results
print(f"Сума чисел: {sum}")
print(f"Добуток чисел: {product}")