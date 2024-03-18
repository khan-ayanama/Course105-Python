# Operator Overloading
# If any operator performs additional action other than what it is meant for, it is called oprator overloading

# Example
# Magic Method
# __add__(self,other)
# __sub__(self,other)
# __mul__(self,other)

class A:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return self.x + other.x

class B:
    def __init__(self,x):
        self.x = x

a = A(100)
b = B(200)

print(a+b)