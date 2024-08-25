# Constructor With Super Method

class Father:
    def __init__(self,m):
        self.money = m
        print("Father Class Constructor")
    
    def show(self):
        print("Father Class Instance Method",self.money)

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)
        self.job = j
        print("Son Class Constructor")
    
    def disp(self):
        print("Son Class Instance Method",self.job)

s = Son(299,'SUN')
s.disp()
s.show()