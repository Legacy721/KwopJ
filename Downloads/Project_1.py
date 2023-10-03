import cv2
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window (it won't be displayed)
root = tk.Tk()
root.withdraw()  # Hide the main root window

# Open a file dialog for selecting a file
file_path = filedialog.askopenfilename()

# Check if a file was selected
if file_path:
    print("Selected file:", file_path)
else:
    print("No file selected")



# Load the image
image_path = "file_path"  
image = cv2.imread(file_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
output_path = "bw_image.jpg"
cv2.imwrite(output_path, gray_image)
image.save("bw_image.jpg")

# Display the grayscale image (optional)
cv2.imshow("Black and White Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

