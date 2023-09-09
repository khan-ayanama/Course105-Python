# Objects and Messages: In OOP, objects communicate with each other by sending messages. A message is a request for an object to perform one of its methods. Objects can interact and collaborate by sending messages to each other.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def start(self):
        print(f"{self.make} {self.model} has started.")

    def accelerate(self, mph):
        self.speed += mph
        print(f"{self.make} {self.model} is now going {self.speed} mph.")

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            print(f"{self.make} {self.model} slowed down to {self.speed} mph.")
        else:
            print(f"{self.make} {self.model} is already stopped.")

# Creating two Car objects
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

# Sending messages (calling methods) to the Car objects
car1.start()  # Output: Toyota Camry has started.
car1.accelerate(40)  # Output: Toyota Camry is now going 40 mph.

car2.start()  # Output: Ford Mustang has started.
car2.accelerate(60)  # Output: Ford Mustang is now going 60 mph.

car1.brake()  # Output: Toyota Camry slowed down to 30 mph.
car2.brake()  # Output: Ford Mustang slowed down to 50 mph.
