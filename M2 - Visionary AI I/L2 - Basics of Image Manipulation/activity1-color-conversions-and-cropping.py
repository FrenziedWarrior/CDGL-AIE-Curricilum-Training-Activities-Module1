import cv2
import matplotlib.pyplot as plt

# Reads the image into memory
image = cv2.imread("M2 - Visionary AI I/L2 - Basics of Image Manipulation/example.jpg")

# Convert BGR to RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display image data as a plot, interpreting values as colors
plt.figure(1)
plt.imshow(image)
plt.title("RGB Image")

# Convert to Grayscale
# INTERNAL OPERATION: Compute a single-channel grayscale image -- GrayPixel = 0.299*R + 0.587*G + 0.114*B
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(2)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")

# Cropping the image
cropped_image = image[100:300, 200:400]

cropped_rgb_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

plt.figure(3)
plt.imshow(cropped_rgb_image)
plt.title("Cropped Region")
plt.show()