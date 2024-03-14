import pygame
import cv2

running = True
pixelSize = 50
numOfLeds = 30 #dont make this larger than the width of the image
times = 0

screen = pygame.display.set_mode((pixelSize * numOfLeds, pixelSize))
pygame.display.set_caption('LEDs')

cam = cv2.VideoCapture(0)

while running:

    result, img = cam.read()
    img = img[(numOfLeds + 1) * -1: -1]
    img = cv2.flip(img, 1)
    
    if result:
        img = cv2.resize(img, (numOfLeds, 1))

        for i in range(len(img)):
            for j in range(len(img[i])):
                pygame.draw.rect(screen, (img[i][j][2], img[i][j][1], img[i][j][0]), pygame.Rect(j * pixelSize, i * pixelSize, pixelSize, pixelSize))
            
        pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           running = False