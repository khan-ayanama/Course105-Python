# Identity Operators
# The identity operators compare the memory locations of two objects. Hence, it is possible to know whether two objects are same or not

# is Operator
x = 5
y = 5
result_is = x is y
print("is Operator:", result_is)  # Output: True

# is not Operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]
result_is_not = list1 is not list2
print("is not Operator:", result_is_not)  # Output: True
