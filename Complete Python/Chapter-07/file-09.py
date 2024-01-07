# replace()
# The replace() method is used to replace occurrences of a specified substring with another string. It returns a new string with the replacements.

original_string = "Hello, World!"

# Using replace() to replace 'Hello' with 'Hi'
modified_string = original_string.replace("Hello", "Hi")

print("Modified String:", modified_string)

# split()
# The split() method is used to split a string into a list of substrings based on a specified delimiter. If no delimiter is specified, it splits the string at whitespace.

sentence = "This is a sample sentence."

# Using split() to split the sentence into words
words = sentence.split()

print("Original Sentence:", sentence)
print("List of Words:", words)

# join()
# The join() method is used to join elements of an iterable (e.g., a list) into a single string. It concatenates the elements with a specified separator.


words = ['This', 'is', 'a', 'sample', 'sentence.']

# Using join() to join the words into a sentence
joined_sentence = ' '.join(words)

print("Joined Sentence:", joined_sentence)

# startswith()
# The startswith() method checks whether a string starts with a specified prefix.

text = "Hello, World!"

# Using startswith() to check if the string starts with "Hello"
starts_with_hello = text.startswith("Hello")

print("Starts with 'Hello'?", starts_with_hello)

# endswith()
# The endswith() method checks whether a string ends with a specified suffix.

filename = "example.txt"

# Using endswith() to check if the filename ends with ".txt"
ends_with_txt = filename.endswith(".txt")

print("Original Filename:", filename)
print("Ends with '.txt'?", ends_with_txt)