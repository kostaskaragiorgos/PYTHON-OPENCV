import cv2

image = cv2.imread("face.jpg")
gr_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_face.jpg",gr_img)