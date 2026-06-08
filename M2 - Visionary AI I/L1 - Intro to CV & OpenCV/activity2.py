import cv2

image = cv2.imread("Module2/Lesson1/example.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (224, 224))

cv2.imshow("Processed Image", resized_image)

key = cv2.waitKey(0)

if key == ord("s"):
    directory = "Module2/Lesson1/"
    filename = directory + "greyscale_resized_image.jpg"
    cv2.imwrite(filename, resized_image)
    print(f"Image saved as {filename}")
else:
    print("Image not saved")

cv2.destroyAllWindows()

print(f"Processed Image Dimensions: {resized_image.shape}")