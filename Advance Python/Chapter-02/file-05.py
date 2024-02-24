# Class Methods
# Class methods are the methods which act upon the class variables or static variables of the class.
# Decorator @classmethod need to write the above the class method
# By default, the first paramter of class method is cls which refers to the class itself.

# Syntax:
# @classmethod
# def method_name(cls,f1,f2):
#     method body

# Example:
class Mobile:
    isPhone=True

    @classmethod
    def is_phone(cls,arg1):
        cls.isPhone = arg1
        return cls.isPhone

    def __init__(self) -> None:
        pass


print(Mobile.is_phone(False))