cats = [10,20,30,10,10]
dogs = [30,10,30,25,35]

catsdogs = []
catsdogs.extend(cats)
catsdogs.extend(dogs)

minmax = []
minmax.append(min(catsdogs))
minmax.append(max(catsdogs))

print(f"Cats & dogs: {catsdogs}\nCats & dogs no duplicates: {list(set(cats+dogs))}\nCats & dogs unique values: {list(set(cats+dogs))}\nCats&Dogs minimum and maximum: {minmax}")