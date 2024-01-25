query = input("Find a word in a sample file: ").lower()

with open('files/sample_four.txt', 'r+') as file:
    data = file.read()
    print(f"Found matches: {data.count(query)}")