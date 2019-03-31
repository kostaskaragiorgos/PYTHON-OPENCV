import cv2
img = cv2.imread("face.jpg")
cv2.imshow("ORIGINAL",img)
rows,cols,ch = img.shape
matrix = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rot_img = cv2.warpAffine(img,matrix,(cols,rows))
cv2.imshow("rot",rot_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
