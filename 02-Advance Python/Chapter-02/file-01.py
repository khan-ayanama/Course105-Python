# Constructor
# It is used for initializing the instance variable of a class.
# It is called whenever a program creates an object.
# It is called only once at the time of creating an instance.
# If two instance are created for a class, the constructorl will be called once for each instance.

# Example:01

class Mobile:
    def __init__(self):
        self.model = 'Nokia'
    

Nokia = Mobile()
print(Nokia.model)


class Car:
    def __init__(self,model,price=5000):
        self.model = model
        self.price = price

Toyota = Car('X-421',340303)
print(Toyota.price)
