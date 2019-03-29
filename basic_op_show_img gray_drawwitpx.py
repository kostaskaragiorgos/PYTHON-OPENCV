import cv2
img = cv2.imread("face.jpg")
img_gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img_gr)
img_gr [175,100] = 255
img_gr [175,101] = 255
img_gr [175,102] = 255
img_gr [175,103] = 255
img_gr [175,104] = 255
cv2.imshow("Face",img_gr)
cv2.waitKey(0)
cv2.destroyAllWindows()