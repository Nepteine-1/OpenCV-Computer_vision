import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([90, 50,50])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([40, 50,50])
    upper_green = np.array([80,255,255])

    lower_red = np.array([0, 125,125])
    upper_red = np.array([20,255,255])

    # Threshold the HSV image to get only blue colors
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    cv.imshow('blue_only', mask1)
    
    mask2 = cv.inRange(hsv, lower_green, upper_green)
    cv.imshow('green_only', mask2)

    mask3 = cv.inRange(hsv, lower_red, upper_red)
    cv.imshow('red_only', mask3)

    final_mask = cv.bitwise_or(mask1,mask2)
    final_mask = cv.bitwise_or(final_mask,mask3)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= final_mask)

    cv.imshow('camera',frame)
    cv.imshow('result',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()