# Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables you to write code that can work with objects of multiple related classes in a uniform way. Polymorphism is often achieved through method overriding and interfaces or abstract classes.

def animal_speak(animal):
    return animal.speak()

# Using polymorphism to call speak method on different objects
print(animal_speak('dog'))  # Output: Buddy says Woof!
print(animal_speak('cat'))  # Output: Whiskers says Meow!
