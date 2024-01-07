# Two Dimensional Array
# If an array contains more than 1 row and 1 column.

# Example:
# Syntax: array_name = array([elements],[elements])
from numpy import *
a = array([[1,2,3,4,5],[5,4,3,2,1]])

# Example: 3-D Array
# Syntax: array([[[elements],[elements]],[[elments],[elements]]])
b = array([[[1,2,3],[3,2,1]],
           [[5,6,7],[7,6,5]]])

# Way of Creating Multi-D Array
# array()
# zeros()
# ones()
# reshape()
print(a[0][1])
print(a[0,1])

# BASIC INDEXING
import numpy as np

# Create a 2-D array
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access a specific element
element = two_d_array[1, 2]
print("Element at (1, 2):", element)

# CHAIN INDEXING

# Access a specific element using double brackets
element = two_d_array[1][2]
print("Element at (1, 2):", element)

# Assign a new value to a specific element
two_d_array[1, 2] = 99
