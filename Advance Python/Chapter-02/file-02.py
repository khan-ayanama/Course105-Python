# Type of Variable
# 1. Instance Variable
# 2. Class Variable/ Static Variable

# INSTANCE VARIABLE
# It's separate copy is created in every object.
# They are defined and initialized using a constructorn with self parameter.

# Example:

class Mobile:
    def __init__(self):
        # Instance Variable
        self.model = 'RealMe X'

    # Accesing instance variable with method
    def show_model(self):
        print("Model: ",self.model)

Phone = Mobile()
Phone.show_model()

# Accessing Variable outside the class
print(Phone.model)