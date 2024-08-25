# Identity operator

a = 100

# Value of a
# print(a)

# Class of a
print(type(a))

# Address of a
print(id(a))

############################################################

a = 100
b = 100

# In python both a and b are at same location due to python memmory allocation algorithm

print(a is b)   # Address is same for both object
print(a is not b)  # Address is different for both objects

# What if we change one of it's value

a = a + 10
# It will allocate new location of a+10, it follows the rule of immutability

# *Note: This type of allocation is not applicable for float and complex data type


# EXAMPLES

# x = [1, 2, 3]
# y = x
# print(x is y)  # Output: True


# p = [1, 2, 3]
# q = p
# q[0] = 100
# print(p)  # Output: [100, 2, 3]


# x = [1, 2, 3]
# y = x
# print(id(x) == id(y))  # Output: True


# a = 5
# b = 5
# print(a is b)  # Output: True (Due to memory optimization)


# x = 100
# y = 100
# print(x is y)  # Output: True (Due to caching)
