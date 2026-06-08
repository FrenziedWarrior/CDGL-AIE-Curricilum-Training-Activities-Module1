import cv2


# Image stores the image as a NumPy array.
# If the image cannot be loaded (e.g., due to incorrect path or file format), image will be None.
image = cv2.imread("Module2/Lesson1/example.jpg")


# Create a string variable to hold `window_name`
window_name = "Loaded OpenCV Window"


# Creates a window where we can display images
# WINDOW_NORMAL flag - makes the window resizable
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)


# Changes the size of the window displaying the image.
# Note that this does not affect the size of the image itself but only the window in which it is displayed.
cv2.resizeWindow(window_name, 800, 500)


# Displays the image in the created window
cv2.imshow(window_name, image)


# Pauses the execution of the code until a key is pressed. 
# The 0 means it waits indefinitely until a key press occurs.
cv2.waitKey(0)


# Closes any OpenCV windows that were created.
# It is essential to release the resources after the image is no longer required.
cv2.destroyAllWindows()


# Gives the dimensions of the loaded image
# Returns a tuple of three values:
# Height (number of rows)
# Width (number of columns)
# Channels (number of color channels, 3 for a colored image: BGR)
print(f"Image Dimensions: {image.shape}")