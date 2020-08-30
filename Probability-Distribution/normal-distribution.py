import matplotlib.pyplot as pdb
import numpy as np

'''Here i plot 100 random values for std normal distribution'''
og_values = np.random.randn(100)
print('Random values =')
print(og_values)
print('max =',max(og_values))
print('min =',min(og_values))
'''plot the histogram'''
pdb.hist(og_values,10)
pdb.show()
'''the above histogram has the mean as zero and sd as 1'''

'''creating a new histogram with using the og_values_shift'''
mean=5
sigma=2
new_values = mean+(og_values*sigma)
print(new_values)
pdb.hist(new_values,10)
pdb.show()