import cv2
import numpy as np
import sys

class Keys:
    KEY_R = ord("r")
    KEY_G = ord("g")
    KEY_B = ord("b")
    KEY_I = ord("i")
    KEY_D = ord("d")
    KEY_Q = ord("q")


def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image.
    
    Parameters:
        image:
        filter_type:

    Returns:
        filtered_image:
    """

    # Create a copy of the image to avoid modifying the original
    filtered_image = image.copy()

    if filter_type == "red_tint":
        # Remove blue, green channels for red tint
        filtered_image[:, :, 1] = 0 # Setting green channel to 0
        filtered_image[:, :, 0] = 0 # Setting blue channel to 0
    
    elif filter_type == "blue_tint":
        # Remove red, green channels for red tint
        filtered_image[:, :, 1] = 0 # Setting green channel to 0
        filtered_image[:, :, 2] = 0 # Setting red channel to 0

    elif filter_type == "green_tint":
        # Remove red, blue channels for red tint
        filtered_image[:, :, 0] = 0 # Setting blue channel to 0
        filtered_image[:, :, 2] = 0 # Setting red channel to 0

    elif filter_type == "increase_red":
        # Increase the intensity of the red channel by a fixed constant
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)

    elif filter_type == "decrease_blue":
        # Increase the intensity of the red channel by a fixed constant
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    return filtered_image


# Load the image
image_path = "M2 - Visionary AI I/L5 - Fun with Filters/example.jpg"
image = cv2.imread(image_path)

# Exit program if image could not be loaded
if image is None:
    sys.exit("Error: Image not found!")

# Default filter type
filter_type = "original"

# Show menu
print("Press one of the following keys to apply the filter:")
print("r - Red Tint")
print("g - Green Tint")
print("b - Blue Tint")
print("i - Increase Red Intensity")
print("d - Decrease Blue Intensity")
print("q - Quit")

while True:
    # Apply the selected filter
    filtered_image = apply_color_filter(image, filter_type)

    # Display the filtered image
    cv2.imshow("Filtered image", filtered_image)

    # Wait for key press
    key = cv2.waitKey(0) & 0xFF

    match key:
        case Keys.KEY_R:
            filter_type = "red_tint"

        case Keys.KEY_G:
            filter_type = "green_tint"

        case Keys.KEY_B:
            filter_type = "blue_tint"

        case Keys.KEY_I:
            filter_type = "increase_red"

        case Keys.KEY_D:
            filter_type = "decrease_blue"

        case Keys.KEY_Q:
            print("Thank you for using Fun with Filters")
            break
            
        case _:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")


cv2.destroyAllWindows()