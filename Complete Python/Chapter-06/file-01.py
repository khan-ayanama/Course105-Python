# ANY and ALL functions

# any(iterable) Function:
# The any function returns True if at least one element in the iterable is True. If the iterable is empty, it returns False.

my_list = [False, True, False]
result = any(my_list)
print(result)  # Output: True


# all(iterable) Function:
# The all function returns True if all elements in the iterable are True. If the iterable is empty, it returns True.

my_list = [True, True, True]
result = all(my_list)
print(result)  # Output: True

my_list = [False, True, True]
result = all(my_list)
print(result)  # Output: False