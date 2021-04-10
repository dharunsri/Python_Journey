from array import *

a = array('i', [])

n = int(input("Size of array: "))

for i in range(n):
    v = int(input("value = "))
    a.append(v)

print(a)

# Search element

s = int(input("Enter search value: "))
k = 0
for e in a:
    if e == s:
        print("value: ",e, "index: ", k)
        break
    k += 1
else:
    print("Not found")

# inbuilt function to get index number:

print(a.index(s))

# Delete value

d = int(input("delete value"))

for j in range(n):
    if a[j] == d:
        del a[j]
        break
else:
    print("No values in the array")
print(a)

# Reverse the array
print("Reversed array")
print(a[::-1])