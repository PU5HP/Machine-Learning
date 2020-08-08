import numpy as np

'''statistics methods in numpy are'''
'''mean vs avg is with weights'''

print('case for 1-d array')
a= np.array([1,2,3,4,5])
print(np.mean(a))
print(np.mean(a,axis=0))
print(np.median(a))
print(np.min(a))
print(np.max(a))
print(np.average(a))
print(np.var(a))

print('case for the 2-d array')
b=np.array([[1,2,3],[6,9,5]])
print(np.mean(b))
print(np.mean(b,axis=1))
print(np.median(b))
print(np.min(b,axis=0))
print(np.max(b,axis=1))
print(np.average(b))
print(np.var(b))

'''mean vs average with weights'''
w = np.array([1,2,3,4,5])
x=np.array([1,2,3,4,5])
print(np.mean(x))
print(np.average(x,weights = w))

'''standard deviation'''
print(np.std(x))
'''variance'''
print(np.var(x))


