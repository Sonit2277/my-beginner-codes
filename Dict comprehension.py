words = ["apple", "banana", "cherry", "date"]

# create dict: word → length of word
length_dict = {word: len(word) for word in words}
print(length_dict)

# create dict: word → word in uppercase
uppercase_dict = {word: word.upper() for word in words}
print(uppercase_dict)
