# Array

from array import *             # It imports everthing from array module

"""
Type Code	C++ Type	            Python Type	            Minimum Sizes in Bytes
‘c’	        char	                character	            1
‘b’	        signed char	            int	                    1
‘B’	        unsigned char	        int	                    1
‘u’	        Py_UNICODE	            unicode character	    2
‘h’	        signed short	        int	                    2
‘H’	        unsigned short	        int	                    2
‘i’	        signed int	            int	                    2
‘I’	        unsigned int	        long	                2
‘l’	        signed long	            int	                    4
‘L’	        unsigned long	        long	                4
‘f’	        float	                float	                4
‘d’	        double	                float	                8
"""

a = array('i',[10,12,-15,2])            # i - signed int (also can store negative values)
print(a)

b = array('I', [2,7,8,1] )              # I - unsigned int (only positive)
print(b)

print(a.buffer_info())                  # prints address and size of the array

b.reverse()
print(b)

ch = array('u', ['a','b','c','d'])
for i in range(len(ch)):
    print(ch[i])

new = array(b.typecode, (n**2 for n in b))
for j in new:
    print(j)


# Sort an array

arr = array('i', [2,10,1,5,3,9,6])
for k in range(len(arr)-1):
    for l in range(k+1,len(arr)):
        if arr[k] >= arr[l]:
            arr[k], arr[l] =arr[l], arr[k]

print(arr)

