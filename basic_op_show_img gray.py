import cv2
img = cv2.imread("face.jpg")
img_gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img_gr)
cv2.imshow("Face",img_gr)
cv2.waitKey(0)
cv2.destroyAllWindows()