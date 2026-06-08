import cv2

image = cv2.imread("Module2/Lesson1/example.jpg")

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize image
resized_image = cv2.resize(gray_image, (224, 224))

cv2.imshow("Resized Grayscale Image", resized_image)

key = cv2.waitKey(0)

print(key)

if key == ord("s"):
    cv2.imwrite('grayscale_resized_rendition.jpg', resized_image)
else:
    print("Image not saved")

cv2.destroyAllWindows()

print(f"Image Dimensions: {resized_image.shape}")