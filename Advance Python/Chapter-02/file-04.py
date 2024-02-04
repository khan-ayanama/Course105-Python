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