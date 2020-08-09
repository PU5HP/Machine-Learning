'''HERE WE ARE PERFORMING MATHEMATICAL OPERATION ON LINEAR ALGEBRA IN NUMPY'''
import numpy as np

#creating a scalar
x =5 

#creating a row vector
y =np.array([1,2,3])
print('row vector =',y)

#creating a column vector
z = np.array([[1],[2],[3]])
print('column vector =',z)

#matrix 2-d
a=np.array([
    [1,2,3],
    [345,455,43],
    [34,23,2]
])
print('matrix:',a)

#tensor
t = np.zeros((5,5,3),dtype='uint8')
print('t =',t)
t[:,:,2]=255
print('new t =',t)

#import matplotlib.pyplot as plt
#plt.imshow(t)
#plt.show()

#transpose 

#case 1:vector
v=np.array([[1],[2],[3],[4]])
print(np.shape(v))
print(np.shape(v.T))

#case 2: 2d matrix
m = np.array([[1,2,3,4],[46,57,7,67],[12,32,3324,4]])
print(m)
print(np.shape(m))
print(m.T)
print(np.shape(m.T))

#tensor
tt= np.zeros((4,5,3))
print(tt)
print(tt.T)
print(np.shape(tt))
print(np.shape(tt.T))
