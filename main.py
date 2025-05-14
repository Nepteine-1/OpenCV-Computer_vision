import numpy as np
import cv2 as cv
 
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
 
def nothing(x):
    pass

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
 
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
 
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(cv.getTrackbarPos('B','image'),cv.getTrackbarPos('G','image'),cv.getTrackbarPos('R','image')),-1)
            else:
                cv.circle(img,(x,y),cv.getTrackbarPos('Radius','image'),(cv.getTrackbarPos('B','image'),cv.getTrackbarPos('G','image'),cv.getTrackbarPos('R','image')),-1)
 
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(cv.getTrackbarPos('B','image'),cv.getTrackbarPos('G','image'),cv.getTrackbarPos('R','image')),-1)
        else:
            cv.circle(img,(x,y),cv.getTrackbarPos('Radius','image'),(cv.getTrackbarPos('B','image'),cv.getTrackbarPos('G','image'),cv.getTrackbarPos('R','image')),-1)


img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

cv.createTrackbar('R','image',0,255,nothing)


cv.createTrackbar('Radius','image',5,45,nothing)
 
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
 

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()