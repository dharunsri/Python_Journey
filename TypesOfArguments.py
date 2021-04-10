# Formal arguments and Actual arguments

# Actual arguments - position, keyword, default, variable length

def student(name, dept = 'cse'):            # default it takes cse
    print(name)
    print(dept)
student('sat', 'cse')          # position

student(dept='cse', name='abi')  # keyword

student('arun')                     # default - if user hadn't give input it takes default value

# variable length
def add(*b):              # *b takes all the arguments as a tuple = so by using *var name we can pass many values to 1 argument
    c = 0
    for i in b:
        c+=i
    print(c)
add(1,4,5,6,3,7)

# keyworded varible length Arguments

def details(name, **data):
    print(name)
    for j,o in data.items():
        print(j,o)
details('DRN', age=19, city='trichy', ph= 34567890)
