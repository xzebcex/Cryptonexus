# ImageBackgroundRemover

# Import necessary modules
from rembg import remove
from PIL import Image

# Define input and output paths
input_path = "input_image.jpg"
output_path = "output.png"

# Attempt to process the image
try:
    # Open the input image using Pillow (PIL)
    input_image = Image.open(input_path)
    
    # Use rembg to remove the background
    output_image = remove(input_image)
    
    # Save the output image with the removed background
    output_image.save(output_path)
    
# Handle any exceptions that may occur
except Exception as e:
    # Print an error message if an exception occurs
    print(f"Error: {e}")
