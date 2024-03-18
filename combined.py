from picamera import Picamera # Use command 'pip install picamera'
from numpy import np # Opencv comes with this so you're fine
import cv2 # Use command 'pip install 'opencv-python'
import board # Idk if we need to install this or if its part of the neopixel library
import neopixel # Use command 'sudo pip install rpi_ws281x adafruit-circuitpython-neopixel'

running = True
numOfLeds = 30 # Don't make this larger than the width of the image

# Creates the pixels array (replace the 18 with the GPIO pin the leds are connected to)
pixels = neopixel.Neopixel(board.D18, numOfLeds)

# Creates the camera and image array
camera = Picamera()
img = np.empty((240, 320, 3), dtype=np.uint8)

while running:

    # Reads image, crops it, and flips it
    camera.capture(img, 'rgb')
    img = img[(numOfLeds + 1) * -1: -1]
    img = cv2.flip(img, 1) # This is only for testing. Remove this in implementation
  
    # Shrinks and pixelates the image
    img = cv2.resize(img, (numOfLeds, 1))

    # Assigns the pixels in img to pygame Rects
    # Remember that opencv (cv2) uses BRG and leds uses RGB
    for i in range(len(img)):
      pixels[i] = (img[i][0][0], img[i][0][1], img[i][0][2])
