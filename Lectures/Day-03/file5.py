# Abstraction: Abstraction is the process of simplifying complex systems by breaking them into smaller, more manageable parts. In OOP, classes and objects are used to represent real-world entities in an abstract manner, focusing on the essential attributes and behaviors.

from abc import ABC, abstractmethod

# Abstract base class for a Shape
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class Circle that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class Rectangle that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Using the abstract methods through the concrete classes
print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
print("Circle Perimeter:", circle.per)
