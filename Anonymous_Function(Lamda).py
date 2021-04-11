# Anonymous function
from functools import reduce

n = int(input("num to square: "))
s = lambda a : a*a
ans = s(n)
print("Square of the number: ",ans)

sum = lambda a,b: a+b
add = sum(10,10)
print("Addition of the num: ",add)

# Filter

nums = [2,4,3,1,8,55,66,22,90]

evens = list(filter(lambda val : val%2==0, nums ))          # filter function filters the values
print(evens)

# Map
doubles = list(map(lambda d : d*2, evens))                  # Map function takes value and apply operation
print(doubles)

# Reduce

s = reduce(lambda a1,a2 : a1+a2, doubles)
print(s)
