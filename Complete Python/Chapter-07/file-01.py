# STRINGS
# Strings are sequences of characters, and they are represented using the str data type. Strings are immutable, meaning that once you create a string, you cannot modify its contents directly.

# CREATING STRING
string1 = 'Hello, World!'
string2 = "Python is awesome."
string3 = '''
    This is 
    multiline 
    string
'''

# When you create a string in Python, memory is allocated to store its characters. The immutability of strings ensures that the memory allocated to a string remains unchanged, and any modifications result in the creation of new string objects. Memory efficiency techniques, such as interning and garbage collection, further contribute to the optimal use of memory in Python.

string1 = 'House'
string2 = 'House' # Now here it will not create a new string it will tag to the previous House
print(id(string1))
print(id(string2))

# INDEXING
my_string = "Python"

# Positive indexing
first_char = my_string[0]
second_char = my_string[1]

# Negative indexing
last_char = my_string[-1]
second_last_char = my_string[-2]

print("First character:", first_char)
print("Second character:", second_char)
print("Last character:", last_char)
print("Second-to-last character:", second_last_char)
