# Set and Get Thread Name

# current_thread() -> Returns current thread object.
# getName() -> name of thread.
# setName(name) -> used to set the name of thread
# name Property -> Get and Set thread name

from threading import Thread,current_thread

def disp():
    print("Child Thread object",current_thread().name)
    current_thread().name = 'Flying Thread'
    print("Child Thread object",current_thread().name)

t = Thread(target=disp)
t.start()

print("Main thread: ",current_thread().name)
