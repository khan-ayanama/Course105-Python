# function returning two values

def func(int1, int2):
    add = int1+int2
    multiply = int1*int2
    return add, multiply


# It will return tuples because function returing more than two values
print(func(2, 3))
add, multiply = func(2, 3)
print(add)


# Something more about tuples, list , str

# tuples using range function
# nums = tuple(range(1, 11))
# print(nums)


# tuples to list
# nums = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(nums)


# tuples to string

# nums = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(nums)
# print(type(nums))
