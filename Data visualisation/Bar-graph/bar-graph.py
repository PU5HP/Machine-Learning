import numpy as np
import matplotlib.pyplot as plt
xcordinates =np.array([1,2,3,4,5])
plt.bar(xcordinates,[10,5,30,10,25],width=0.25,label='current year',color='orange',tick_label=['gold','silver','zinc','bronze','graphite'])
plt.bar(xcordinates+0.25,[40,20,60,10,15],width=0.25,color='blue',label='next year')
plt.xlabel('Metals')
plt.ylabel('Prices')
plt.title('metal vs prices')
plt.style.use('dark_background')
plt.plot()
plt.legend()
plt.show()

