# Array
import numpy as np

y = np.array([1,2,3,4])
print(y)
print(type(y))

# Dimensions in Arrays
# 1-D --> [1,2,3]
# 2-D --> [[1,2,3]]
# 3-D --> [[[1,2,3]]]

arr1 = np.array([1,2,3])
print(arr1.ndim)

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.ndim)

# Array of 10 dimension
arr3 = np.array([1,2,3,4],ndmin=10)
print(arr3)
print(arr3.ndim)