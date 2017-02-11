import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

img1 = cv2.rectangle(img,(111,111),(400,400),(0,0,100),3)

plt.imshow(img1)

plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()