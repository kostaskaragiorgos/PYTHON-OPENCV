import cv2

img = cv2.imread("face.jpg")
scal_img = cv2.resize(img, (100,100))
cv2.imshow("scal",scal_img)
cv2.imshow("ORIGINAL",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
