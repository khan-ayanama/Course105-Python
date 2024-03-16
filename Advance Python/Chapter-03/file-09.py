# Hierarchical Inheritance
# When one parent class has more than one child class

class Father:
    def __init__(self):
        print("Father Class Constructor")
    def showF(slef):
        print("Fahter class Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")
    def showS(self):
        print("Son class Method")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter Class Constructor")
    def showD(self):
        print("Daughter Class Mehtod")

# Son Class
s = Son()
s.showS()
s.showF()

# Daughter Class
d = Daughter()
d.showD()
d.showF()