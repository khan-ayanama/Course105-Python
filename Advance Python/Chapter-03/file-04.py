# Declaration of Child Class
# class ChildClassName(ParentClassName):
#     members of Child class

# Single Inheritance
# If class is derived form one base class, called single inhertance

# Example
class Father:
    money = 1000

    def show(self):
        print("Parent class Instance Method")

    @classmethod
    def show_money(cls):
        print("Parents class method money: ",cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent Class Static Mehthod: ",a)
    
class Son(Father):
    def disp(self):
        print("Child Class Instance Method")

s = Son()
s.disp()
s.show()
s.show_money()
s.stat()