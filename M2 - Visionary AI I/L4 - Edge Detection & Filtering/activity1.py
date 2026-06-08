import cv2
import numpy as np
import matplotlib.pyplot as plt

"""Utility function to display an image"""
def display_image(title, image):
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

"""Interactive activity for edge detection and filtering"""
def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    print("Select an option: ")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        # SOBEL EDGE DETECTION
        if choice == "1":
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))

            # 1. Take absolute value and convert to uint8 safely
            # abs_sobel_x = cv2.convertScaleAbs(sobel_x)
            # abs_sobel_y = cv2.convertScaleAbs(sobel_y)

            # 2. Blend them together accurately
            # combined_sobel = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
            display_image("Sobel Edge Detection", combined_sobel)

        # CANNY EDGE DETECTION
        elif choice == "2":
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_threshold = int(input("Enter lower threshold: "))
            upper_threshold = int(input("Enter upper threshold: "))
            edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)
            display_image("Canny Edge Detection", edges)
        
        # LAPLACIAN EDGE DETECTION
        elif choice == "3":
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))
        
        # GAUSSIAN SMOOTHING
        elif choice == "4":
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size(odd number): "))
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Smoothed Image", blurred)

        # MEDIAN FILTERING
        elif choice == "5":
            print("Adjust kernel size for Median Filtering (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size(odd number): "))
            median_filtered = cv2.medianBlur(image, kernel_size)
            display_image("Median Filtered Image", median_filtered)
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


interactive_edge_detection("M2 - Visionary AI I/L4 - Edge Detection & Filtering/example.jpg")