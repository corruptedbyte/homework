def isPalindrome(num):
    numStr = str(num)
    if (numStr[::-1] == numStr):
        return True
    return False

print(isPalindrome(1011))