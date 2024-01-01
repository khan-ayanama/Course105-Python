# Methods of array

# 1. append()
# This method is used to add an element at the end of the existing array.
# array_name.append(new_element)

# Example:
from array import *

student_roll = array('i',[1,2])
student_roll.append(2)
for element in student_roll:
    print(element)

# 2. insert()
# This method is used to insert an element in a particular position of the exisiting array and shift the element at that postion.
# Syntax: array_name.insert(position,new_element)
student_roll.insert(1,23)

# 3. pop()
# This method is used to remove last element from existing array and returns it.
ans = student_roll.pop()
# print("ANS",ans)
# student_roll.pop()
# student_roll.pop()
for element in student_roll:
    print("yehai",element)

# pop(n): This method is used to remove an element specified by position number and returns element

# 4. remove()
# This method is used to remove first occurence of given element from an existing array. If it doesn't found the element, shows valueError
student_roll.remove(1)

# 5. index()
# This method retuns position number of first occurence of given element in an array. If it doesn't found the element, shows valueError
student_roll.index(2)

# 6. reverse()
# This method is used to reverse the order of elements in the array.
student_roll.reverse()

# 7. extend()
# This method is used to append another array or iterable object at the end of array
extra_numbers = array('i',[5,6,7])
student_roll.extend(extra_numbers)

# Slicing on Arrays
# Slicing on arrays can be used to retrive a piece of array that contains group of elements. Slicing is useful to retrieve a range of elements.
# new_array_name = array_name[start:stop:step]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice from index 2 to 6 (exclusive)
result = my_list[2:6]
print(result)  # Output: [3, 4, 5, 6]

result = my_list[3]
print(result)  # Output: 4

# You can also specify step size
result_with_step = my_list[1:8:2]
print(result_with_step)  # Output: [2, 4, 6, 8]
