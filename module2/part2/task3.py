# Here we will convert m (meters) into cm (cantimeters)

# So, 1m = 100cm
# We'll multiply the user input by 100

meters = int(input("Метри: "))

millimeters = meters * 1000
cantimeters = meters * 100
decimeters = meters * 10
miles = meters * 0.00062137

print(f"Міліметри: {millimeters}")
print(f"Сантиметри: {cantimeters}")
print(f"Дециметри: {decimeters}")
print(f"Милі: {miles}")