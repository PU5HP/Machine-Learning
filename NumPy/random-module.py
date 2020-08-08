'''RANDOM MODULE IN PYTHON'''
import numpy as np
a = np.arange(10) + 2
print(a)

'''shuffle function'''
print('THE SHUFFLED ARRAY IS AS:')
np.random.shuffle(a)
print(a)

'''creating a random array'''
b = np.random.rand(2,3)
print(b)
'''creating an array from the random distribution'''
c =np.array(2)
c=np.random.randn(c)
print(c)
'''creating array by choosing from the random integers:'''
d =np.random.random_integers(2,4,(8,8))
print(d)
'''selecting a particular element'''
f=np.array([1,32,3,43,3,5,34,23,34])
element = np.random.choice(f)
print(element)