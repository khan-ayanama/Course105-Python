# Creating a thread without using a class

# from threading import Thread
# thread_object = Thread(target=function,args=(arg1,arg2,...))

# thread_object -> It represents our thread
# target -> It represents the function on which the thread will act.
# args -> It represent a tuple of arguments which are passed to the function

# Example:-
from threading import Thread

def disp(a,b):
    print("Thread child running!",a,b)

# Creating & Starting a thread
t1 = Thread(target=disp,args=(10,20))
t1.start()

# Creating & Starting a thread
t2 = Thread(target=disp,args=(5,34))
t2.start()

# Program in main thread
for i in range(5):
    print("Main Thread")

# In the above example there are three threads
# 1. Main thread which started other two threads t1 and t2