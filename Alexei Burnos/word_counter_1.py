import string
import re

words = input()
new_word1s = [i for i in re.split(rf"[{string.punctuation + string.whitespace + string.digits}]+", words) if i != '']
print(*new_word1s)
print(len(new_word1s))
