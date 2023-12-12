# This one is a bit of pain, so i'm going to recieve the numbers by processing them as integers, but then I will combine them into a string and convert them back into one integer.

# Getting the values
x = int(input("Число 1: "))
y = int(input("Число 2: "))
z = int(input("Число 3: "))

# The tricky part :)
# Combining the values (putting them in a string)
combined = f"{x}{y}{z}"


# To turn them into integer and work with them simply do:
# int(combined)
# This way you can manipulate the number.

#Printing the output
print(combined)