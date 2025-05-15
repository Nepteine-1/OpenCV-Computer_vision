import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
def setCanny(x):
    global edges
    edges = cv.Canny(img,cv.getTrackbarPos('Gradient 1','image'),cv.getTrackbarPos('Gradient 2','image'))
    cv.imshow('image', edges)

img = cv.imread('wallpaper.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

cv.namedWindow('image')
edges = cv.Canny(img,100,200)

cv.createTrackbar('Gradient 1', 'image', 0,300, setCanny)
cv.createTrackbar('Gradient 2', 'image', 0,300, setCanny)

while 1:
    cv.imshow('image', edges)
    cv.waitKey(0)