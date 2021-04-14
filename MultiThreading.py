# Multithreading - run multiple task at the same time

# importing threading module to make it as thread

from threading import *
from time import sleep

# Now this whole program considered as Main thread
class sample1(Thread):          # Now this class becomes a thread

    def run(self):              # here we used run() - a inbuilt method of threading
        for i in range(5):
            print("Good Morning")
            sleep(0.5)

class sample2(Thread):              # Now this class is a thread

    def run(self):
        for i in range(5):
            print("Good night")
            sleep(0.5)


obj1 = sample1()
obj2 = sample2()
# SO in total we have 3 thread Main thread, obj1 thread, obj2 thread

obj1.start()        # here the start() calls a inbuilt method called run() in threading
sleep(0.1)
obj2.start()

obj1.join()             # this will make the 2 threads to be completed
obj2.join()

print("Finished")           # this will be printed by main thread