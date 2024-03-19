import pygame # Use command 'pip install pygame'
from picamera2 import Picamera2 # Use command 'pip install picamera'
import numpy as np # Python comes with this so you're fine
import cv2 # Use command 'pip install 'opencv-python'

running = True
pixelSize = 50
numOfLeds = 30 # Don't make this larger than the width of the image

# Creates the pygame window
screen = pygame.display.set_mode((pixelSize * numOfLeds, pixelSize))
pygame.display.set_caption('LEDs')

# Creates the camera and image array
camera = Picamera2()

camera.start()

while running:

    # Reads image, crops it, and flips it
    img = camera.capture_array()
    img = img[(numOfLeds + 1) * -1: -1]
    img = cv2.flip(img, 1) # This is only for testing. Remove this in implementation
  
    # Shrinks and pixelates the image
    img = cv2.resize(img, (numOfLeds, 1))

    # Assigns the pixels in img to pygame Rects
    # Remember that opencv (cv2) uses BRG and pygame uses RGB
    for i in range(len(img)):
        for j in range(len(img[i])):
            pxl = pygame.Rect(j * pixelSize, i * pixelSize, pixelSize, pixelSize)
            pygame.draw.rect(screen, (img[i][j][2], img[i][j][1], img[i][j][0]), pxl)
        
    # Draws everything to the screen
    pygame.display.flip()
    
    # Makes the pygame 'X' work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           running = False

camera.stop()
