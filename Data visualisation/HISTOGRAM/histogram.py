import numpy as np
import matplotlib.pyplot as plt

Xsn = np.random.randn(100)
sigma =5
mean =60
X =np.round(Xsn*sigma+mean)
print(X)
plt.hist(X)
plt.plot()
plt.show()

