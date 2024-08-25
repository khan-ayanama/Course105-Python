# Constructor Overriding
# If we defined a constructor in child class then it will override the class constructor

class Father:
    def __init__(self):
        self.money = 999
        print("Father Constructor")
    def show(self):
        print("Father Instance")

class Son(Father):
    def __init__(self):
        self.money = 499
        print("Son Class Constructor")
    
    def disp(self):
        print("Son Class Constructor")

s = Son()
print(s.money)
s.disp()
s.show()