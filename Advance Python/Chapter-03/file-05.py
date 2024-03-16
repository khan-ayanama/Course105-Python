# Constructor in Inheritance
# By default The constructor in the parent class is availble in child class 

class Father:
    def __init__(self,m):
        self.money=m
        print("Father Class Constructor")

    def show(self):
        print("Father class Instance MEthod")


class Son(Father):
    def disp(self):
        print("Son Class Instance Method")


s = Son(994)
print(s.money)
s.show()
s.disp()