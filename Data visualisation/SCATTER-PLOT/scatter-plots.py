import numpy as np
import matplotlib.pyplot as plt

'''Ploting a graph when only one axis is given'''

prices = np.array([1,2,3,4,5,6])**3
print(prices)
plt.plot(prices)
plt.plot()
plt.show()
# when only one axis is given then it is taken as y -axis

'''CREATING A SCATTER-PLOT GRAPH'''
x = np.array([1,2,3,4,5,6])
y =np.array([10,34,5,3,2,32])
y2=np.array([100,14,25,33,212,3])
plt.figure(figsize=(2,2))
print("x =",x)
print("y =",y)
plt.scatter(x,y,marker='o')
plt.scatter(x,y2,marker='*')
plt.xlabel('time')
plt.ylabel('growth')
plt.title('time v/s growth')
#adjust size of any plot
plt.figure(figsize=(2,2))
plt.legend()
plt.show()