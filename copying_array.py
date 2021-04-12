from numpy import *

a = array([1,4,6,9,3,5])
a2 = array([3,4,9,6,1,6])
a+=5
print(a)

a3 =a+a2
print(a3)

# Mathematical operations
# sin
print(sin(a))

# cos
print(cos(a2))

# log
print(log(a3))

# min, max
print(min(a))
print(max(a2))

# sort
print(sort(a))

# concatenation
print(concatenate([a,a2]))

# Copying methods

a4 = a
print(a4)
print(id(a4))
print(id(a))            # having same address - aliasing - which means only one array in 2 different variables

# shallow copy
a5 = a.view()
print(a5)               # changes affect both arrays

# deep copy
a6 = a.copy()
print(a6)               # makes a new array and won't depend each other
