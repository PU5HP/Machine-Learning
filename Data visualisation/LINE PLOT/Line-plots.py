import numpy as np
import matplotlib.pyplot as plt

'''In this program we plot lines on the graphs by specifying the x axis array and y axis array'''

'''PLOT AN GRAPH Y =X**2'''

x = np.arange(10)
print('x = ',x)
y = x**2
print('y =',y)
#data-visualization_1.png
#plt.plot(x,y)
#plt.show()

'''PLOT 2 lines on the same graph'''
y1 = 2*x+3
#plt.plot(x,y1,y)
print('y1 =',y1)
#plt.show()
#data-visualization_1.png

'''THEMES FOR REPRESENTATION OF THE GRAPH'''
themes = plt.style.available
print(themes)
'''USING A SPECIFIC THEME FOR THE REPRESENTATION OF THE GRAPH'''
#plt.style.use("seaborn-dark")
#plt.plot(x,y,color ='red')
#by passing the color for the arguement we can specify the color of the graph
#plt.show()

'''FULL DESCRIPTIVE GRAPH'''
plt.plot(x,y,color='red',label='apple',marker='o')
plt.plot(x,y1,color='green',label='kiwi',linestyle='dashed')
plt.title("price of fruits with time")
plt.xlabel("time")
plt.ylabel("fruit")
plt.legend()
plt.show() 









