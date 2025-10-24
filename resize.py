from PIL import Image
import os

# Open the image
img_path = 'images/36743b5a-d372-4f9c-9aea-70492c5a7511.jpeg'
img = Image.open(img_path)

# Resize to a suitable size for hero background, e.g., 1200x800
img = img.resize((1200, 800), Image.Resampling.LANCZOS)

# Save the resized image
img.save(img_path)
