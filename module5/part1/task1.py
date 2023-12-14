palindrome = input("Enter a sentence or a word: ")

if (palindrome == palindrome[::-1]):
    print(f"\"{palindrome}\" is a palindrome")
else:
    print(f"\"{palindrome}\" isn't a palindrome")