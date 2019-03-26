import cv2

image = cv2.imread("face.jpg")
cv2.imshow("FACE",image)
cv2.waitKey(0)
cv2.destroyAllWindows()