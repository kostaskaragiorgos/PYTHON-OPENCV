import cv2
img = cv2.imread("face.jpg")
cv2.imshow("ORIGINAL",img)
scl_img = cv2.resize(img,None , fx = 1 ,fy = 1/2)
cv2.imshow("SCALED",scl_img)   
cv2.waitKey(0)
cv2.destroyAllWindows()
