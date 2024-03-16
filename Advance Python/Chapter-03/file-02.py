# Nested Class
# A class withing a class is called as nested class or nesting of a class
# Example:

class Army:
    def __init__(self):
        self.name = 'Rahul'
        self.gn = self.Gun()

    def show(self):
        print("Name: ",self.name)

    class Gun:
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 Rounds'
            self.length = '34.3 In'
        
        def disp(self):
            print("Gun Name: ",self.name)
            print("Gun Capcity: ",self.capacity)
            print("Gun Length: ",self.length)


a = Army()
print(a.name)
a.show()

print(a.gn.name)

g = a.gn
# g = Army().Gun()
print(g.name)
print(g.capacity)
print(g.length)