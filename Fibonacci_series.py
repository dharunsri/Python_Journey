# fibonacci series
n = int(input("Enter series length: "))
def fibo(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    elif n == 0:
        print(b)
    elif n<0:
        print("Invalid Number")
    else:

        print(a)
        print(b)

        for i in range(2,n):
            c = a+b
            a = b
            b = c
            if c>n:
                break
            print(c)
fibo(n)