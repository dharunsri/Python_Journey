# Recursion - Function calls itself again & again

import sys
a = sys.getrecursionlimit()             #  Maximum limit is 1000
b = sys.setrecursionlimit(2000)         #  We can change it
print(a)

i = 0
def itself():
    global i
    i+=1
    print("hi",i)
    itself()

#itself()

# Factorial using Recursion
x = int(input("Number to find factorial: "))
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
ans = fact(x)
print(ans)