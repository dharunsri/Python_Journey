from numpy import *

m = array([
            [5,6,2,1,4,9],
            [8,1,9,10,18,56]

          ])
print(m)
print(m.dtype)              # datatype of the array
print(m.ndim)               # dimension of array - here, 2 dimenional array
print(m.shape)              # shape - 2*3
print(m.size)               # total size of array - 6

m2 = m.flatten()            # converts 2d into 1d array
print(m2)

m3 = m2.reshape(3,4)        # converts 1d to multi d array
print(m3)


# Matrix Function & Operations
mat1= matrix('1,2,3;4,5,6; 7,8,9')
mat2 = matrix('2,5,3;1,5,8;22,12,33')
mat3 = mat1+mat2
print(mat1)
print()
print(mat3)
print(mat1*mat2)

