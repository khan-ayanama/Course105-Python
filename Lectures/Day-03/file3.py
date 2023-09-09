# Inheritance: Inheritance allows you to create a new class (subclass or derived class) that inherits properties and behaviors from an existing class (base class or superclass). It promotes code reuse and the creation of hierarchical relationships between classes.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects of the Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method of the derived classes
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!


# Types of Inheritance
# 1. Single
# 2. Multiple
# 3. Hybrid
# 4. Heirarichal

