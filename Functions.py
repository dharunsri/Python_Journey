def wish():                                 # fuction definition - def
    print("Hi everyone!")
    print("This is a function.")
wish()                                     # function calling

print()

a = int(input())
b = int(input())
def mat(a,b):
    c = a+b
    d = a-b
    return c,d

ans1, ans2 = mat(a,b)
print(ans1,'\n',ans2)