# NONZERO Function
# It is used to determine the position of element which are non-zero. 
# It returns an array of indexex of the element which are not zero.

# Syntax: numpy.nonzero(array_name)
from numpy import *
a = array([1,2,3,0,5])
c = nonzero(a)
print(c)