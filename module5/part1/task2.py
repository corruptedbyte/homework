text = input("Enter a sentence: ").lower().replace(",", "")
reserved = input("Enter words to capitalize in the sentence (Split the words with a coma: word,word): ").split(',')

textSplit = text.split()

for i in range(0, len(textSplit)):
    if textSplit[i] in reserved:
        print(textSplit[i].upper())