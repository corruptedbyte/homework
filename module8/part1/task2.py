vowels = ["a", "e", "i", "o", "u"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
consonants = ["c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "q", "s", "t", "v", "x", "z"]

with open("files/sample.txt", "r+") as file:
    data = file.read()
    lines = len(file.readlines())

    vowelcount = 0
    numbercount = 0
    consonantcount = 0

    print(f"Symbol count: {len(data)}")
    print(f"Line count: {lines}")
    for char in data.lower():
        if char in vowels:
            vowelcount += 1
    for char in data.lower():
        if char in consonants:
            consonantcount += 1
    for char in data.lower():
        if char in numbers:
            numbercount += 1
    

    print(f"Number of vowels: {vowelcount}")
    print(f"Number of consonants: {consonantcount}")
    print(f"Number count: {numbercount}")