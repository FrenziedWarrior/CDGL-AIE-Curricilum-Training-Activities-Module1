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

        # CANNY EDGE DETECTION
        elif choice == "2":
        
        # LAPLACIAN EDGE DETECTION
        elif choice == "3":
        
        # GAUSSIAN SMOOTHING
        elif choice == "4":

        # MEDIAN FILTERING
        elif choice == "5":
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


filepath = "M2 - Visionary AI I/L4 - Edge Detection & Filtering/example.jpg"
interactive_edge_detection(filepath)