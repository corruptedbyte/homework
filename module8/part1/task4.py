with open("files/sample_three.txt") as file:
    print(f"Size of last line: {len(file.readlines()[-1])} characters")