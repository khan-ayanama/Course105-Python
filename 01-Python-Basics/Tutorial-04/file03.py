# In Python, functions do not actually return values by value. Instead, they return values by reference. This means that when you return a value from a function, you're returning a reference to the memory location where the value is stored. This behavior applies to all types of values, whether they are simple types like integers and strings or more complex objects like lists and dictionaries.
def modify_list(my_list):
    my_list.append(4)

original_list = [1, 2, 3]
modify_list(original_list)

print(original_list)  # Output: [1, 2, 3, 4]


# To work with values independent of their original references, you would need to create copies of the values. For example, to avoid modifying the original list within the function, you could make a copy of the list before modifying it:
def modify_list_copy(my_list):
    modified_list = my_list.copy()
    modified_list.append(4)
    return modified_list

original_list = [1, 2, 3]
modified_list = modify_list_copy(original_list)

print(original_list)    # Output: [1, 2, 3]
print(modified_list)    # Output: [1, 2, 3, 4]
