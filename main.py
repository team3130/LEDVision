import pygame
import cv2

running = True
pixelSize = 50
numOfLeds = 30 # Don't make this larger than the width of the image

# Creates the pygame window
screen = pygame.display.set_mode((pixelSize * numOfLeds, pixelSize))
pygame.display.set_caption('LEDs')

# Creates the camera using its id (webcam id's are 0)
cam = cv2.VideoCapture(0)

while running:

    # Reads image, crops it, and flips it
    result, img = cam.read()
    img = img[(numOfLeds + 1) * -1: -1]
    img = cv2.flip(img, 1) # This is only for testing with a webcam. Remove this in implimentation
    
    # Variable result is a boolean of whether or not the camera returned an image
    # This if statement prevents the code from crashing if the camera stops for a few frames
    if result:
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