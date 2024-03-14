import pygame
from cv2 import *

screen = pygame.display.set_mode((10, 100))
pygame.display.set_caption('LEDs')

cam = VideoCapture(0)

result, img = cam.read()
img = img[0:11]

while True:
    result, img = cam.read() 
    
    if result:
        img = cv2.resize(img, (10, 1))

        for i in range(len(img)):
            pygame.draw.rect(screen, img[0][i], pygame.Rect(i * 10, i * 10, 10, 10))
            
        pygame.display.flip()