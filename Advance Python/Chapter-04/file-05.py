# Mehtod Overriding
# if same method is in parent and child class then child class method takes precedence

# Witout super method
# class Add:
#     def result(self,a,b):
#         print('Addition: ',a+b)

# class Multi(Add):
#     def result(self,a,b):
#         print("Multplication: ",a*b)

# m = Multi()
# m.result(10,20)

# With super method
class Add:
    def result(self,a,b):
        print('Addition: ',a+b)

class Multi(Add):
    def result(self,a,b):
        # Calling parent class result method
        super().result(a,b)
        print("Multplication: ",a*b)

m = Multi()
m.result(10,20)