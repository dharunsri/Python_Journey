#Abstract Class and method

# python doesn't support abstract method by default so we use abc(abstract base class) module

from abc import ABC, abstractmethod

class selena():                 # the class which has abstract method is called abstract class
    @abstractmethod
    def info(self):         # nothing in a method is called abstract method
        pass

# we can't create a object in abstract class

class Taylor(selena):

    def info(self):             # without defining anything in this class then it also becomes an abstract method
        print("Taylor swift")


t = Taylor()

t.info()