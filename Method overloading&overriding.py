# There is no method overloading concept in python
# Because we can't create 2 methods with same name

# But creating 2 methods with same name but in different class - method overriding

#overloading but in different way
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a = None, b = None, c = None):
        if a!=None and b!=None and c!=None:
            m = a+b+c
        elif a!=None and b!=None:
            m = a+b
        else:
            m = a

        return m

s1 = student(20,10)

print(s1.sum(5,2))


# Method Overriding

class A:

    def show(self):
        print("In method A")

class B(A):                                         # In this class it takes show() method from Class A
    pass

class C(B):                                         # here it has same method name as in class A. This is called method overriding

    def show(self):
        print("In Method C")


x = B()
x2 = C()
x.show()
x2.show()