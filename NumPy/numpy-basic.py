import numpy as np

# arrays in numpy
a = np.array([1,2,3,4,5])
print(a)                    # [1,2,3,4,5]
print(type(a))             #<class 'numpy.ndarray'>
print(a.shape)             #(5,)     linear one-dimensional-array
#this contains 5 colums and one row =====>(5,)

#multi-dimensional array
b = np.array([[1],[2],[3],[4],[5]])
print(b)                  #[[1][2][3][4][5]]
print(type(b))           #<class 'numpy.ndarray'>
print(b.shape)           #(5,1)    two dimensional array
# this contains 5 rows and 1 column =====> (5,1)

'''one [] represent a row'''
c=np.array([[1,3],[2,4],[3,4]])
print(c.shape)        
#this contains 3 rows and 2 columns =======>(3,2)

''' ACCESSING THE NUMPY ARRAYS'''
print(a[3])               #4
print(b[1][0])            #2       
print(c[1][1])            #4
'''THE numpy arrays are mutable'''
a[3]=69
print(a[3])

'''CREATE SPECIFIC ARRAYS IN NUMPY'''
#array of zeros or NULL matrix
d =np.zeros((2,3))
print("NULL Matrix =",d)
#array of ones 
e =np.ones((3,4),dtype = np.int64)
print('unit matrix =',e)
#array of specific number matrix
f=np.full((3,4),99)
print(f)
#indentity matrix (always square matrix)
g=np.eye((5))
print('IDENTITY MATRIX =',g)
#random matrix 
h=np.random.random((2,3))
print('Random matrix:',h)

'''SLICING IN NUMPY ARRAYS'''
print('sliced array:',h[:,1:3])
h[:,1:3] = 100
print('transformed array =',h)

'''DATA-TYPES IN NUMPY'''
print(e.dtype)
print(e)

'''ELEMENT OPERATIONS ON NUMPY ARRAY'''

m = np.array([[1,2],[3,4]])
n = np.array([[5,6],[7,8]])

'''ADDITION - ELEMENT'''
print(m+n)
print(np.add(m,n))


'''subtraction - ELEMENT'''
print(m-n)
print(np.subtract(m,n))


'''Multiplication - ELEMENT'''
print(m*n)
print(np.multiply(m,n))


'''division - ELEMENT'''
print(m/n)
print(np.divide(m,n))


'''addtion - ELEMENT - by axis'''
print('by axis')
print(np.sum((m,n),axis=1))

'''matrix multiplication'''
print(np.dot(m,n))

'''array stacking'''
print('stacking')
asx = np.array([1, 2, 3])
bsx = np.array([2, 3, 4])
print(np.stack((asx, bsx),axis=1))#along y axis ==>column wise
print(np.stack((asx,bsx),axis=0))#along x axis  ==>row wise

'''array reshape function'''
cc= np.array([[1,2,3,4],[5,6,7,8]])
print('cc =',cc)
print(np.reshape((cc),(4,2)))
print(np.reshape((cc),(8,1)))
print(np.reshape((cc),(-1,8)))



























