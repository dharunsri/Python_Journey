# In python there is no pass by value or pass by reference

def update(x):            # In this function the values are immutable and they have different address so changes won't affect
    print(id(x))
    x = 8

    print(id(x))
    print(x)

a = 10
print(id(a))
update(a)
print(a)


def change(b):          # In this function list is a muttable and they have same address so changes affects
    print(id(b))
    b[1] = 100

    print(id(b))
b = [10,11,1000]
print(id(b))
change(b)
print(b)
