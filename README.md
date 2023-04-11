# Random-Image-Generator:
This Python code uses the PIL (Python Imaging Library) module to create a new image with random RGB pixel values. The image dimensions are set to 640 x 480. The code generates random pixel values and assigns them to each pixel location. Finally, the image is saved as a PNG file named "random_image.png".

## Pre-requisite modules:
**PIL :** It is the Python Imaging Library

  Example:

` pip install Pillow `

## Steps:
1.The code starts by importing the Image and random modules.
 
2.The code then creates a new image with dimensions of 640x480 pixels.
 
3.Next, it loads the image into memory using the `load()` method from PIL's Image module.
 
4.It then iterates through each pixel in the image to create a random color value between 0 and 255 for each pixel.
 
5.The next line saves the newly created image to disk as `random_image.png`.
 
6.The code creates an Image object with the dimensions of `640x480 pixels`.
 
7.The next step in the code is to load the image into memory and then iterate through every pixel on the screen, assigning each pixel a random value between `0 and 255`.
