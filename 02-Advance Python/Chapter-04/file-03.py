# Strong Typign
# If the object has method or not 

# hasattr(object,attribute)

class Duck:
    def walk(self):
        print("thapak thapak thapak" )


class Horse:
    def walk(self):
        print("TABADAK TABKDAAk")

class Cat:
    def talk(self):
        print("Meow Meow")

def myFunction(obj):
    # Strong typing
    if hasattr(obj,'walk'):
        obj.walk()
    
    if hasattr(obj,'talk'):
        obj.talk()
    

d = Duck()
myFunction(d)

c = Cat()
myFunction(c)