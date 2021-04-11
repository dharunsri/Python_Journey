# Defining own module

def even(a):
    return a%2==0

def odd(a):
    return a%2!=0

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def fact(n):
    if n ==0:
        return 1

    return n*fact(n-1)

def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    elif n == 0:
        print(b)
    elif n<0:
        print("Invalid input")

    else:
        print(a)
        print(b)
        for i in range(n):
            c = a+b
            a = b
            b = c
            if c>n:
                break
            return c


