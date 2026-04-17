import cv2

image=cv2.imread('C://Users//USER//Downloads//example.jpg')

cv2.namedWindow('loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('loaded Image', 10, 10)

cv2.imshow('Loaded Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")