# Method Overloading
# When more than one method of same name is defined in same class called method overloading.

# There is no overloading in python
# class Myclass:
#     def sum(self,a):
#         print('1st Sum Method',a)
    
#     def sum(self):
#         print("2nd Sum Method")

# obj = Myclass()
# In both cases later sum method will be called.
# obj.sum()
# obj.sum(10)


# Method Overloading
class Myclass:
    def sum(self,a=None,b=None,c=None):
       if a!=None and b!=None and c!=None:
           return a+b+c
       elif a!=None and b!=None:
           return a+b
       else:
           return a
    
    
obj = Myclass()
print(obj.sum(2,3,4))