import cv2
import matplotlib.pyplot as plt

selena = cv2.imread('selena.jpg')
'''pyplot reads images as BGR but we want to get the image as RGB'''
new_selena = cv2.cvtColor(selena,cv2.COLOR_BGR2RGB)
plt.imshow(selena)
plt.show()
plt.imshow(new_selena)
plt.show()