import cv2

image = cv2.imread('wallpaper.jpg')

if image is None:
    print("Erreur : Impossible de charger l'image.")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

edges = cv2.Canny(blurred_image, 50, 150)

cv2.imshow('Image Originale', image)
cv2.imshow('Contours', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()