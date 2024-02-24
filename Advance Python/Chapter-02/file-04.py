# Types of Methods

# 1. INSTANCE METHOD
    # Accessor methods
    # Mutator Methods

# 2. CLASS METHODS

# 3. STATIC METHODS


# Instance Method
# Instance methods act upon instance varaibles, these methods need to know the memory address of the instance which is self

class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    # Instance method 
    def show_model(self,price):
        self.price = price
        print(self.model,self.price)

    # Instance method with parameter
    def show_price(self,price):
        print(f"{self.model} and Price: {price}")


# Acessor or Getter Method
# It is a convention this method is used to retrive or get the data from instance it's not that we can't modify data but we don't.
# Example:
        
class Dog:
    def __init__(self):
        self.breed = 'Pug'
    
    # Getter Method
    def get_breed(self):
        return self.breed
    

# Mutator or settor method
# It is also a convention just like getter method

class Tractor:
    def __init__(self):
        self.model = 'Mahindra 365'
    
    # Setter method
    def set_model(self):
        self.model = 'Swaraj 365'
    
