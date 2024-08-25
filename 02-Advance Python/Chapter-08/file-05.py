# Creating a Thread by creating a child class to Thread class from threading module.

from threading import Thread

class MyThread(Thread):
    def run(self):
        print("Run Method")


t= MyThread()
t.start()
t.join()
print(t.name)

# Method's of Thread class
# start() 
# run() -> When program starts run method called
# join() -> when you want to execute thread first