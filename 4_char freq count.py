from collections import Counter
def char_freq(str):
    return Counter(str)
str = "hello"
print(char_freq(str))