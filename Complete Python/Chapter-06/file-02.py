# WHERE FUNCTION
# It creates a new Array which contains, returned element chosen from expression1 or expression2:
# Syntax numpy.where(condition,expression1,expression2)

from numpy import *
# Example:01
a = array([100,200,300,400,500])
b = array([10,20,30,40,50])
c = where(a<b,a,b)
print("answer is ",c)



# Exmaple:02
arr = array([1, 2, 3, 4, 5])
indices = where(arr > 2) 

# print(indices)

# In this example, numpy.where returns a tuple of arrays containing the indices where the condition arr > 2 is true. The output will be something like (array([2, 3, 4]),), indicating that the elements at indices 2, 3, and 4 satisfy the condition.


# You can also use numpy.where to assign values based on a condition:
arr = array([1, 2, 3, 4, 5])
new_arr = where(arr > 2, arr, 0)
print(arr)
print(new_arr)

# In this case, elements greater than 2 are retained, and others are replaced with 0. The output will be [0, 0, 3, 4, 5].