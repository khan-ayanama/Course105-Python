# IMPORTING NUMPY
# There are two ways:

# 1. Import entire numpy module
# import numpy

# 2. Import all class, objects variables etch from numpy package.
# from numpy import *

# ONE DIMENSIONAL ARRAY
# num = [1,2,3,4,5]

# WAYS TO CREATE ARRAY IN NUMPy
# array()
# linspace()
# logspace()
# zeros()
# ones()
# arange()

# array() Function
# numpy.array(object,dtype=None, copy=True, order='K',subok=False,ndmin=0)

# Creating 1D Array using array() Function
# import numpy
# array_name=numpy.array([elements])

# Method:01
# import numpy 
# student_roll = numpy.array([1,2,3,4,5])
# student_roll = numpy.array([1,2,3,4,5],int)
# student_roll = numpy.array([1,2.5,3,4,5],float)

# Method:02
# from numpy import *
# array_name = array([elements])

# INDEXING
# Example-01
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# element = arr[2]  # Access the element at index 2
# print(element)   # Output: 3

# Example-02
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
subarray = arr[1:4]  # Access elements from index 1 to 3
print(subarray)     # Output: [2, 3, 4]
