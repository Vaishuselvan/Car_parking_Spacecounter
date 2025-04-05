import cv2
import pickle

img = cv2.imread('car-parking.png')

while True:
    cv2.imshow('Image',img)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break