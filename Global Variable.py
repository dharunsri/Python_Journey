# Scope - Local & Global

a = 10                                  # Global variable can use anywhere in the program

def temp():
    a = 20                              # Local variable can access only inside a function

    print("Local",a)

temp()


print("Global",a)


def change():
    global a
    a = 15
    print("Global changed",a)
change()
print("global", a)

b = 10
print(id(b))
def scope():
    b = 20
    c = globals()['b']
    print(id(c))

    print("local b", b)

    globals()['b'] = 15

scope()
print("global b",b)
