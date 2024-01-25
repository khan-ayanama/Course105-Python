# CONSTRUCTOR

# Constructor is a special method used for initializing the attributes of an object when it is created.
# The constructor method is named __init__, and it is automatically called when you create an instance of a class.
# It allows you to set up the initial state of the object by specifying parameters that are used to initialize instance variables.

class Dog:
    # Constructor method
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5


# NOTE:
# self parameter is a convention in Python and represents the instance of the class. It must always be the first parameter in the method, but when you call the method, you don't explicitly pass a value for self – Python takes care of that behind the scenes.