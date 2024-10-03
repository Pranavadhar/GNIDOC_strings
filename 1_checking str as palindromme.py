def is_palindrome(str):
    return str == str[::-1]
str = "racecar"
print(is_palindrome(str))