# Class --> Attribute + Methods
# Attributes --> variable that contains data.
# Method --> Method performs an action or task.

class Dog:
    # Class attribute
    species = "Canine"

    # Constructor method (initialization)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and calling methods
print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} belongs to the {Dog.species} species.")
dog1.bark()
dog2.bark()


# NOTE:
# class keyword is used to create a class
# object represents base class name, it's optional.
# self is a variable which refers to current class instance/object.
# __init__(), it is used to initialize varaibles, we not need to call this explicitly.
# Class name generally starts with Capital letter.