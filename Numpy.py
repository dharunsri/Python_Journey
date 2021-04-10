from numpy import *

# array()

a = array([1,3,6,4,8,2,5],float)
print(a)
print(a.dtype)

# linspace()

l = linspace(0,10,20)    # linspace takes 3 parameters - start, end, and range to split
print(l)

# arange()

a2 = arange(1, 20, 2)           # arange - start , stop, iteration
print(a2)

# logspace()

l2 = logspace(1,50,3)               # here it spits in logorithmic method
print(l2)
print('%.2f' %l2[1])

# zeros()

z = zeros(5)
print(z)

# ones()
o = ones(5, int)
print(o)