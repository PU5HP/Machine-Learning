import numpy as np
import matplotlib.pyplot as plt
'''MAKING A PIE CHART'''
subjects =np.array(['maths','english','punjabi','hindi','farsi'])
student =np.array([12,3,32,21,2])
plt.pie(student,explode=(.1,.1,0,0,0),labels=subjects,autopct='%f%%',shadow=True,frame=True)
plt.style.use('dark_background')
plt.plot()
plt.show()

