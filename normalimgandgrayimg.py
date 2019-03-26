import cv2

image = cv2.imread("face.jpg")
gr_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("FACE",image)
cv2.imshow("GRAY FACE",gr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()