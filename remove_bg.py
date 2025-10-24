from PIL import Image
import os

# Path to the image
img_path = 'images/1845ff3e-1f9a-4902-9170-90cb25a1fae8.jpeg'
output_path = 'images/1845ff3e-1f9a-4902-9170-90cb25a1fae8.png'

# Open the image
img = Image.open(img_path).convert('RGBA')

# Get data
datas = img.getdata()

new_data = []
for item in datas:
    # Change all white (also shades of whites) pixels to transparent
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

# Update image data
img.putdata(new_data)

# Save as PNG
img.save(output_path, 'PNG')
print(f"Background removed and saved as {output_path}")
