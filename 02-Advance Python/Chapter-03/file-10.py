# Multiple Inheritance
# If a class is derived from more than one parent class

class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Class Constructor")
    def showM(self):
        print("Mother Class Method")

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")

s = Son()
s.showS()
s.showM()
s.showF()

# Method Resolution Order (MRO)
# In the multiple inheritance scenario members of class are searched first in the current class. If not found, the search continues into parent classes in depth-first, left to right manner without searching the same class twice.

# s = Son()
# THe search will start from Son. As the object of Son iscreated, the constructor of Son is called.
# Son has super().__init__() inside it's constructor so it's parent class, the one in the left side "Father" class's constructor is called
# Father class also  has super().__init__() inside it's constructor so it's parent 'object' class's contructor is called.
# Object doesn't have any constructor so the search will continue down to right hand side class(Mother) of object class so MOther class's constructor is called.
# As Mother class also has super methodd so it's parent calss object contructir is called but as object class alreadey visited, the search will stop here.