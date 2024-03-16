# Multilevel Inheritance

class Father:
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        super().__init__()  # Father Class Constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Instance Method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()  # Calling Son Class Constructor
        print("GrandSon Class Constructor")
    def showG(self):
        print("GrandSon Class Instance Method")


g = GrandSon()
g.showG()
g.showF()
g.showS()

