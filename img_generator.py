from PIL import Image
import random

# Image dimensions
width = 640
height = 480

# Create a new image with random pixel values
img = Image.new('RGB', (width, height))
pixels = img.load()

for i in range(width):
    for j in range(height):
        pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Save the image
img.save('random_image.png')