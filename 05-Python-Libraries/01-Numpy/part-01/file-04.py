# Special NumPy Array
import numpy as np

# Array filled with ZEROES
# 1-D
arr_zero = np.zeros(4)
print(arr_zero)

# 2-D
arr_zero_2_dimension = np.zeros((3,4))
print(arr_zero_2_dimension)


# Array filled with ONES
arr_one = np.ones(4)
print(arr_one)

# Empty Array
arr_empty = np.empty(4)
print(arr_empty)

# Range Array
arr_range = np.arange(4)
print(arr_range)

# Array Diagonal filled with 1's
arr_dig = np.eye(3)
print(arr_dig)

# Array with particular space
arr_space = np.linspace(0,10,num=5)
print(arr_space)