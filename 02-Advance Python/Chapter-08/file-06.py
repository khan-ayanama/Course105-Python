# Thread Child Class with Constructor

from threading import Thread

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Child Thread constructor")
    def run(self):
        pass

t = MyThread(10)
t.start()

print("Main Thread")