# Duck Typing
# Python doesn't care about which class or object it is, in order to call an existing method on an object. IFf the method is defined on the object then it will be called

class Duck:
    def walk(self):
        print("thapak thapak thapak" )


class Horse:
    def walk(self):
        print("TABADAK TABKDAAk")


def myFunction(obj):
    obj.walk()

d = Duck()
myFunction(d)

h = Horse()
myFunction(h)