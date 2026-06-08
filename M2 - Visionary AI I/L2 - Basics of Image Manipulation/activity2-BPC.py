import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = ""
image = cv2.imread(filename)

# Convert BGR to RGB

plt.figure(1)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow

plt.figure(2)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()