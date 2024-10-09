import re

input_str = input("Enter a string of words separated by commas, periods, and spaces: ")

words = re.split(r'[,. ]+', input_str)
words = [word for word in words if word]

min_word = min(words, key=len)
max_word = max(words, key=len)

print(f"Smallest word: {min_word}")
print(f"Largest word: {max_word}")
