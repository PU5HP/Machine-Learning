import matplotlib.pyplot as pdb
import numpy as np

'''Here i plot 100 random values for std normal distribution'''
og_values = np.random.randn(100)
print('Random values =')
print(og_values)
sigma =2
mean = 5
new_val = mean + (sigma*og_values)
x = new_val
y =np.zeros(x.shape)
#print('y=',y)
#print(y.shape)
pdb.scatter(x,y)
pdb.show()