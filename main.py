import cv2 as cv

im = cv.imread('logo.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray,200,255,0)
cv.imshow('rte', thresh)
contours, hier = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(im, contours, -1, (0,255,0), 3)

cv.imshow('test',im)
cv.waitKey(0)