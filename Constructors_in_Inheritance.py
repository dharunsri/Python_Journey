# Constructors in inheritance

class A:

    def __init__(self):
        print("In A init")


    def something(self):
        print("In Class A")

class B:

    def __init__(self):

        print("In B init")


    def Something(self):
        print("In Class B")

class C(A,B):                                       # Multiple Inheritance

    def __init__(self):
        super().__init__()                          # It calls A class only. Becoz of MRO(method resolution order) - it goes from left to right. so c to a to b
        print("In C init")

b = C()

b.something()