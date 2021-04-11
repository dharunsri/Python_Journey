# Factorial of a number

n = int(input("Enter the number for factorial: "))

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    print(f)

x = n
fact(x)