# View Method
# It is used to construct new view of array with same data of existing array. Th existing array and new array will share differetn memory locations.
# If the new array get modified, the existing will also be modified as the elements in both the arrays will be like mirror image

# Example
from numpy import *

a = array([1,2,3,4,5])
b = a.view()