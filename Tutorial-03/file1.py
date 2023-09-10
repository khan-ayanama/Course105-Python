# A list is a versatile and commonly used data structure that can hold a collection of items. It's defined using square brackets [] and can contain elements of different types. Here's how you can create and manipulate lists in Python:

# ############# LIST    #################

# list is data structure
# ordered collection of items
# can store anything like int, float, string

# you can declare list same as arrays in javascript

# numbers = [1, 2, 3, 4]
# print(numbers)

mixed = [1, 2, 3, 4.0, 'name', None]
# print(mixed)

# print(mixed[2])
# print(mixed[:2])

# mixed[1] = 'new'
# print(mixed)

mixed[2:] = ['three', 'four']
print(mixed)


# in keyword with list

# fruits = ["orange", "apple", "pear", "banana", "kiwi"]

# for fruit in fruits:
#     print(fruit)

# if "apple" in fruits:
#     print("present")
# else:
#     print("Not present")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
