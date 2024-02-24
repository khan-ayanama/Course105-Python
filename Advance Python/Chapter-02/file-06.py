# Static Methods
# It is used for some processing related to class but does not need the class or instance to perform any work
# Decorator @staticmethod need to write above the static method

# Syntax:
# @staticmethod
# def method_name(f1,f2):
#     method_body

# Example:
class Mobile:
    @staticmethod
    def show_model(model,price):
        model = model
        price = price
        print(model,price)

Mobile.show_model('tractro',40000)