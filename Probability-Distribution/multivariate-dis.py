import numpy as np
import matplotlib.pyplot as plt

'''IN multivariate distribution the data is stored as two different variables'''

cov1= np.array([[1,0],[0,1]])
mean =np.array([0.0,0.0])

cov2= np.array([[30,0.4],[0.1,6]])
mean2 =np.array([3.0,8.0])
'''cov2=[[spread x axis,yx reation],[x,y relation,spread y axis]]'''
dist = np.random.multivariate_normal(mean,cov1,500)
dist2 = np.random.multivariate_normal(mean2,cov2,500)
plt.scatter(dist2[:,0],dist2[:,1],marker='*')
plt.scatter(dist[:,0],dist[:,1])
plt.show()