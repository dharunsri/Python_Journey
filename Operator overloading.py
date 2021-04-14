# Operator  overloading
# calling or defining the exist method is operator overloading here


a = 10
b = 10
print(a+b)

print(int.__add__(a,b))                     # each datatytpe declared as class and operators have seperate class and methods

print(str.__add__("10","10"))


print(type(a))                              # Thats y while getting type of a variable it denotes <class 'int'>


class studendts:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = studendts(m1,m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1>r2:
            return True
        else:
            return False

    def __str__(self):                                  # we are oveloading the exist method
        return "{} {}".format(self.m1, self.m2)

s1 = studendts(30,35)
s2 = studendts(40,56)

s3 = s1+s2                          # we need to declare add method else it won't work
print(s3.m1, s3.m2)

if s1>s2:
    print("s1 wins")
else:
    print("S2 wins")


print(s1)


# we are calling a method for every operation [ex:  + = __add__(self,other)]