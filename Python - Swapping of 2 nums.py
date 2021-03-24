# Swapping of two numbers

a = 10         # 1010
b = 20         # 10100

# Method 1

temp = a
a = b
b = temp

print(" Swapping using a temporary variable is : " ,'\n',a, '\n',b)

# Method 2

a = a+b             # 10 + 20 = 30
b = a-b              # 30 - 20 = 10
a = a-b              # 30 - 10 = 20

print(" Swapping without using a temporary variable is : ",'\n', a ,'\n', b)

"""Sometimes the bits can be lost
     for example,
               5 = 101
               6 =110
               while swapping = 5 + 6 = 11 -> 1010  [ got 4 bits of 3 bits value. Losing a bit]
"""

# Method 3
# XOR method - here the losing of bits can be avoided
a = a^b        
b = a^b         
a = a^b

print("Swapping without using a temporary variable and without losing a bit: ", '\n',a ,"\n", b)

"""
xor works as - if the bit is,   0 in the second variable first will be the ans or if the bit is 1 in the second variable complement of 1st is ans

 for example,
        10 - 01010
        20 - 10100
               11110 - 30
     so the swapping will perform like this
 """


# Method 4
# Simple way - Rot2 method (rotation 2 | 2 rotation method)

a,b =b,a

print("Swapping in a simple way without using temporary variable : ", '\n',a ,"\n", b)


