import numpy as np

#NORMS 
a = np.array([3,4])
lp2 = np.linalg.norm(a)
# basically in lp2 norms we just square and add the number of the given vectors
print(lp2)   #==>5
# incase of the lp1 norm we just add the absolute sum of the numbers
lp1 = np.linalg.norm(a,ord=1)
print(lp1)   #==>7
#incase of the infinity norm we can find the largest number in the vector
lpinf = np.linalg.norm(a,ord=np.inf)
print(lpinf) #==>4

#determinant of the matrix
m = np.array([[1,2], [3,4]])
print(np.linalg.det(m)) #==>-2
    
#inverse of a matrix when det is not eqaul to zero
print(np.linalg.inv(m))
# a * a(inverse) = identity matrix
print(np.dot(m,np.linalg.inv(m)))

'''IF THE DETERMINANT IS ZERO THEN WE FIND PSUEDO INVERSE FOR THE MATRIX'''
x = np.array([[1,0],[2,0]])
print(np.linalg.det(x)) #==>0
#print(np.linalg.inv(x))  ===> shows an errors as det is zero
print(np.linalg.pinv(x))

'''psuedo inverse and the other inverse is the same cause if the det is not zero
if the det is zero we can only find the psuedo inverse'''