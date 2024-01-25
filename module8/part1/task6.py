query = input('What word to replace? > ')
query2 = input('What to replace it with? > ')

filePath = "files/sample_five.txt"

with open(filePath, "r+") as file:
    data = file.read()
    dataProcessed = data.replace(query, query2)
    file.seek(0)
    file.write(dataProcessed)
    file.truncate()