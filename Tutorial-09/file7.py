# Variable part2  and Excercise

class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Ayan', 'Khan', 20)
p2 = Person('Ayan', 'Khan', 20)
p3 = Person('Ayan', 'Khan', 20)
p4 = Person('Ayan', 'Khan', 20)
print(Person.count_instance)
