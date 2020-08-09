'''Broad casting refers to adding a scalar to vector or adding a vector to the matrix'''

#Adding scalar to a vector
import numpy as np

v = np.array([1,2,3,4])
s = 5
print("v + s = ", v+s)

#Adding a vector to a matrix
m = np.array([[1,2,3,4],[3,4,5,6]])
print("m + v =",m+v)

'''HADAMARD PRODUCT ==> it is the element -wise multoplication of the matrix'''
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[0,1],[0,3]])
print(m1*m2)

'''MATRIX MUTIPLICATION'''
print(np.dot(m1,m2))


