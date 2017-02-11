import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px

# cv2.line params = img, start, end, RGB, thickness
img = cv2.line(img,(0,0),(256,256),(0,255,0),5)

plt.imshow(img)
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()