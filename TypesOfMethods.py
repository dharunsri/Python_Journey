# Instance method, Class method, Static method
# Instance method - Accessor and Mutator method

class students():

    school = "xyz"                                    # static variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):                                      # Instance Method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):                                   # getters - only fetch the value -> Accessors
        return self.m1

    def set_m1(self,val):                               # setters - change the value -> Mutators
        self.m1 = val

    @classmethod                                        # decorators
    def getSchool(cls):                                      # class method
        return cls.school

    @staticmethod                                      # decorators
    def info():                                         # static method - Nothing do with class method or instance method. just to use for some specific operations(ex: factorial, fibonacci series)
        print("This is a static method")

s1 = students(45,40,50)
s2 = students(45,49,38)

print(s1.avg())

print(students.getSchool())